# Challenge 1: Data Preprocessing for Multilingual Garment Orders

## Overview

This project involves preprocessing order data from international buyers, which includes text in multiple languages (English, Bangla, Hindi, and Chinese). The goal is to preprocess this data for input into a Large Language Model (LLM) by normalizing and translating the text data.

## Approach and Methodology

1. **Language Detection**: Identify the language of each text field using the `langid` library.
2. **Translation**: Translate non-English text into English using the `GoogleTranslator` from the `deep_translator` library.
3. **Normalization**: Convert all text to lowercase and remove special characters.
4. **Missing Data Handling**: Appropriately handle missing or empty text fields.

## Technologies, Libraries, and Frameworks Used

- **Python**: Programming language used for implementation.
- **Pandas**: Data manipulation and analysis.
- **LangID**: Language detection.
- **Deep Translator**: Translation service (Google Translator).
- **Regular Expressions (re)**: For text normalization.

## Instructions for Setting Up the Environment and Running the Code

1. **Clone the Repository**: Clone the project repository to your local machine.
    ```bash
    git clone <https://github.com/sojib96/Coding-Challenges.git>
    cd <aI-mL-engineer>
    cd <challenge-1>
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

5. **Run the Code**: Execute the provided script to preprocess the order data.
    ```bash
    python data_preprocessing.py
    ```


## Results

The script processes the input DataFrame by translating non-English text to English, normalizing all text fields, and handling missing data. The output is a DataFrame with all text fields in English and normalized format. The result will be displayed in the command line when you run the script.

**Expected Result:**

```plaintext
   order_id product  quantity special_instructions
0         1  tshirt      1000           rush order
1         2   jeans       500          needed fast
2         3   shirt       750    standard shipping

