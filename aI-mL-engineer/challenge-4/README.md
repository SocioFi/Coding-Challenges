# Labor Law Compliance Classification

This project demonstrates the fine-tuning of a pre-trained language model (BERT) to classify text snippets as compliant or non-compliant with Bangladesh labor laws and international standards. The project involves fine-tuning the BERT model on a synthetic labeled dataset and implementing an inference pipeline for real-time classification.

## Approach and Methodology

The project is divided into two main parts:
1. **Model Fine-Tuning**: 
    - A BERT model is fine-tuned on a synthetic dataset of text snippets labeled as either compliant or non-compliant.
    - The fine-tuning process involves loading the pre-trained BERT model, tokenizing the text data, and training the model using a custom training loop.
    - The fine-tuned model is saved for later use.

2. **Inference Pipeline**:
    - A Streamlit web application is developed to classify new text snippets.
    - The app loads the fine-tuned model and tokenizer to process input text and output a compliance classification with a confidence score.

## Technologies, Libraries, and Frameworks Used

- **Python**: The primary programming language used.
- **Transformers (Hugging Face)**: Used for loading pre-trained BERT models and tokenizers.
- **PyTorch**: Backend framework for training and inference.
- **Pandas**: For dataset manipulation and preprocessing.
- **Scikit-Learn**: For splitting the dataset and calculating evaluation metrics.
- **Datasets (Hugging Face)**: To create and manage the dataset during the fine-tuning process.
- **Streamlit**: For building the web-based user interface for text classification.

## Instructions for Setting Up the Environment

1. **Clone the Repository**: Clone the project repository to your local machine.
    ```bash
    git clone <https://github.com/sojib96/Coding-Challenges.git>
    cd <aI-mL-engineer>
    cd <challenge-4>
    ```

2. **Create a Virtual Environment**: Set up a virtual environment to manage dependencies.
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```

4. **Install Dependencies**: Install the required Python libraries.
    ```bash
    pip install -r requirements.txt
    ```


### Running the Fine-Tuning Script

1. **Dataset Preparation**: 
   - Ensure your dataset is in a CSV file named `labor_law_compliance_dataset.csv` in the same directory.
   - The dataset should have two columns: `text` (the text snippet) and `label` (0 for non-compliant, 1 for compliant).

2. **Fine-Tuning the Model**:
    ```bash
    python LLM_finetuning.py
    ```
   - The model and tokenizer will be saved in the `./model` directory after training.

### Running the Inference Pipeline

1. **Start the Streamlit App**:
    ```bash
    streamlit run app.py
    ```

2. **Using the App**:
   - Enter the text snippet you want to classify in the text area provided in the web interface.
   - Click "Classify" to see the predicted class (compliant or non-compliant) and the confidence score.

## Assumptions and Limitations

- The dataset used for fine-tuning is a small, synthetic dataset created for demonstration purposes. Performance might differ on larger, real-world datasets.
- The fine-tuned model is trained only for 1 epoch, so performance might not be the up to mark.
