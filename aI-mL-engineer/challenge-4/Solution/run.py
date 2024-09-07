import torch
import os
import gdown
import numpy as np
import pandas as pd
import argparse
import sys
from tabulate import tabulate
from transformers import AutoTokenizer, AutoModel
from text_preprocess import text_preprocessing_pipeline

# Argument Parsing
parser = argparse.ArgumentParser(description="Classify text for labor law compliance.")
parser.add_argument("--model-path", default="model.pth", help="Path to the model file.")
parser.add_argument("--target-path", default="labor_law_compliance_dataset.csv", help="Path to the target CSV file.")
parser.add_argument("--result-path", default="result.csv", help="Path to store the results.")
parser.add_argument("--display", default=True, help="Display the result CSV in terminal.")
args = parser.parse_args()

# Model Path
MODEL_PATH = args.model_path

# Check if the model file exists; download if not
if not os.path.isfile(MODEL_PATH):
    url = 'https://drive.google.com/uc?id=1Z_nlxYjxfRQAC64rc3T_l9Zvvg3lKrly'
    gdown.download(url, MODEL_PATH, quiet=False)

# Set device to GPU if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Define BERT-based model
class BERTClass(torch.nn.Module):
    def __init__(self):
        super(BERTClass, self).__init__()
        self.roberta = AutoModel.from_pretrained('roberta-base')
#         self.l2 = torch.nn.Dropout(0.3)
        self.fc = torch.nn.Linear(768,2)
    
    def forward(self, ids, mask, token_type_ids):
        _, features = self.roberta(ids, attention_mask = mask, token_type_ids = token_type_ids, return_dict=False)
#         output_2 = self.l2(output_1)
        output = self.fc(features)
        return output


# Load model
print("### Loading model ###")
model = BERTClass()
try:
    model=torch.load("model.pth", weights_only=False,map_location=torch.device(device))
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    sys.exit()

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained('roberta-base')

def pred_text(process_text: str):
    map_class = ["Non Compliant", "Compliant"]
    
    # Tokenize the input text
    inputs = tokenizer.encode_plus(
        process_text,
        truncation=True,
        add_special_tokens=True,
        max_length=200,
        padding='max_length',
        return_token_type_ids=True
    )
    
    ids = inputs['input_ids']
    mask = inputs['attention_mask']
    token_type_ids = inputs["token_type_ids"]

    # Convert to tensors and move to device
    ids = torch.tensor(ids, dtype=torch.long).unsqueeze(0).to(device)
    mask = torch.tensor(mask, dtype=torch.long).unsqueeze(0).to(device)
    token_type_ids = torch.tensor(token_type_ids, dtype=torch.long).unsqueeze(0).to(device)
    
    # Set the model to evaluation mode
    model.eval()
    with torch.no_grad():
        output = model(ids, mask, token_type_ids)
    
    # Apply softmax to get probabilities for each class
    probs = torch.nn.functional.softmax(output, dim=1).cpu().numpy()[0]
    
    # Return the predicted class and the confidence score
    return {
        'class': map_class[np.argmax(probs)],  # Predicted class
        'confidence': max(probs)  # Confidence of the predicted class
    }

def process_csv(target_df, output_file='result.csv', display=True):
    """Process CSV file and classify each text entry."""
    result_df = pd.DataFrame()

    for idx, txt in enumerate(target_df['text']):
        process_text = text_preprocessing_pipeline(txt)
        result = pred_text(process_text)
        result.update({'text': txt})

        temp_df = pd.DataFrame([result], index=[idx])
        result_df = pd.concat([result_df, temp_df])

    # Save results to CSV
    result_df.to_csv(output_file, index=False)
    print(f"### Results stored to {output_file} ###")

    # Display in terminal if requested
    if display:
        print(
            tabulate(
                result_df,
                headers=result_df.columns,
                floatfmt=".5f",
                showindex=True,
                tablefmt="psql",
            )
        )

if __name__ == "__main__":
    # Load the target CSV
    try:
        target_df = pd.read_csv(args.target_path)
        process_csv(target_df, args.result_path, args.display)
    except FileNotFoundError:
        print(f"Error: File {args.target_path} not found.")
    except Exception as e:
        print(f"Error processing CSV: {e}")
