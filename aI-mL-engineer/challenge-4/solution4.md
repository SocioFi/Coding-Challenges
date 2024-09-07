# Fine-tuning a Text Classification Model using Transformer

## Brief Explanation of Approach
This solution uses a Transformer-based model (BERT or RoBERTa) to perform text classification. The model is fine-tuned using a labeled dataset of text snippets related to labor law compliance. The fine-tuning process involves adjusting the model weights to minimize classification loss, enabling the model to accurately classify new text data.

## Assumptions
- The dataset `compliance_texts.csv` contains properly labeled text samples for training.
- The environment has GPU support for efficient training of transformer models.

## Instructions to Run
1. Install the required dependencies using `requirements.txt`.
2. Load the dataset and run the `solution4.py` file to fine-tune the model.
3. Use the trained model to predict compliance on new text data.

## List of Dependencies and Versions
- Python 3.7+
- `transformers` >= 4.20.0
- `torch` >= 1.10.0
- `pandas` >= 1.3.0
- `numpy` >= 1.21.0

## Requirements
### `requirements.txt`
