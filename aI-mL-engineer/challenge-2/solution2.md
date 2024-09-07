# LLM Fine-tuning for Compliance Checking

## Brief Explanation of Approach
The script fine-tunes a pre-trained language model (such as BERT or RoBERTa) using a dataset labeled with compliance or non-compliance regarding labor laws. The fine-tuning process adjusts the model weights to improve its ability to classify texts according to the given labels. Additionally, a function is provided to classify new text and return a compliance score.

## Assumptions
- The dataset `labor_law_compliance_dataset.csv` contains valid labeled text data.
- The pre-trained model (e.g., BERT) is accessible from Hugging Face's Transformers library.

## Instructions to Run
1. Install the necessary dependencies using `requirements.txt`.
2. Load the dataset and run the `solution2.py` file to start the fine-tuning process.
3. Use the `classify_text` function to classify new texts for compliance.

## List of Dependencies and Versions
- Python 3.7+
- `transformers` >= 4.20.0
- `torch` >= 1.10.0
- `pandas` >= 1.3.0

## Requirements
### `requirements.txt`
