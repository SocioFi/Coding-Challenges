import pandas as pd
import numpy as np
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

class BertModelFineTuner:
    def __init__(self, dataset_file_name, model_name='bert-base-uncased', num_labels=2):
        self.dataset_file_name = dataset_file_name
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertForSequenceClassification.from_pretrained(model_name, num_labels=num_labels)

    def loadDataset(self):
        dataset = pd.read_csv(self.dataset_file_name)
        return train_test_split(dataset, test_size=0.2, stratify=dataset['label'])

    def preprocessFunction(self, examples):
        return self.tokenizer(examples['text'], padding='max_length', truncation=True)

    def computeEvaluationMetrics(self, eval_pred):
        logits, labels = eval_pred
        predictions = np.argmax(logits, axis=-1)
        precision, recall, f1, _ = precision_recall_fscore_support(labels, predictions, average='binary')
        accuracy = accuracy_score(labels, predictions)
        return {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1': f1
        }

    def trainModel(self, train_dataset, eval_dataset):
        training_args = TrainingArguments(
            output_dir='./results',
            evaluation_strategy="epoch",
            learning_rate=2e-5,
            per_device_train_batch_size=8,
            per_device_eval_batch_size=8,
            num_train_epochs=1,
            weight_decay=0.01,
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            compute_metrics=self.computeEvaluationMetrics
        )

        trainer.train()
        self.model.save_pretrained('./model')
        self.tokenizer.save_pretrained('./model')

    def main(self):
        train_df, eval_df = self.loadDataset()
        train_dataset = Dataset.from_pandas(train_df)
        eval_dataset = Dataset.from_pandas(eval_df)

        train_dataset = train_dataset.map(self.preprocessFunction, batched=True)
        eval_dataset = eval_dataset.map(self.preprocessFunction, batched=True)

        self.trainModel(train_dataset, eval_dataset)

if __name__ == "__main__":
    trainer = BertModelFineTuner(dataset_file_name='labor_law_compliance_dataset.csv')
    trainer.main()
