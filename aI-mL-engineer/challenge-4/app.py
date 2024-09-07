import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax
import numpy as np

class InferencePipeline:
    def __init__(self, model_path):
        self.tokenizer = BertTokenizer.from_pretrained(model_path)
        self.model = BertForSequenceClassification.from_pretrained(model_path)

    def classifyText(self, texts):
        inputs = self.tokenizer(texts, return_tensors='pt', padding=True, truncation=True)
        outputs = self.model(**inputs)
        logits = outputs.logits
        probabilities = softmax(logits, dim=-1)
        predictions = probabilities.argmax(dim=-1)
        confidence_scores = probabilities.max(dim=-1).values
        return predictions.tolist(), confidence_scores.tolist()

def main():
    st.title("Text Classification with BERT")

    model_path = './model'
    predictor = InferencePipeline(model_path)
    
    st.header("Input Text")
    user_input = st.text_area("Enter text here:", "Overtime is compensated as per law.")
    
    if st.button("Classify"):
        if user_input:
            texts = [user_input]
            predicted_classes, confidence_scores = predictor.classifyText(texts)
            st.write(f"**Predicted Class:** {predicted_classes[0]}")
            st.write(f"**Confidence Score:** {confidence_scores[0]:.4f}")
        else:
            st.write("Please enter text to classify.")

if __name__ == "__main__":
    main()
