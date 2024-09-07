import pandas as pd
import re
from langdetect import detect
from googletrans import Translator


def preprocess_multilingual_data(df):
    translator = Translator()

    def detect_and_translate(text):
        if pd.isnull(text):  # Handle missing data
            return ""
        try:
            # Detect language
            lang = detect(text)
            # Translate to English if not already in English
            if lang != 'en':
                translated = translator.translate(text, src=lang, dest='en')
                return translated.text
            else:
                return text
        except Exception as e:
            print(f"Error in translation: {e}")
            return text  # Return original text if detection/translation fails

    def normalize_text(text):
        text = text.lower()  # Convert to lowercase
        text = re.sub(r'[^a-z0-9\s]', '', text)  # Remove special characters, keep alphanumeric and spaces
        return text

    # Apply language detection, translation, and normalization to all text columns
    text_columns = df.select_dtypes(include=['object']).columns  # Select text columns only

    for col in text_columns:
        df[col] = df[col].apply(detect_and_translate).apply(normalize_text)

    return df


# Sample input
data = pd.DataFrame({
    'order_id': [1, 2, 3],
    'product': ['T-shirt', 'জিন্স', '衬衫'],
    'quantity': [1000, 500, 750],
    'special_instructions': ['Rush order', 'দ্রুত প্রয়োজন', 'Standard shipping']
})

# Preprocess the DataFrame
preprocessed_data = preprocess_multilingual_data(data)
print(preprocessed_data)
