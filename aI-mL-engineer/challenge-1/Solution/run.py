import pandas as pd
from langdetect import detect
from deep_translator import GoogleTranslator
import re

def translate_text(text, source_lang):
    try:
        # Translate the text to English
        translated = GoogleTranslator(source=source_lang, target='en').translate(text)
        return translated
    except Exception as e:
        return text  # Return the original text in case of translation failure

def detect_and_translate(text):
        if pd.isnull(text):  # Handle missing data
            return ""
        try:
            # Detect language
            lang = detect(text)
            if lang != 'en':
                translated = translate_text(text, lang)
                return translated
            else:
                return text
        except Exception as e:
            return text # If any error occurs return original text
def normalize_text(text):
        text = text.lower()  # Convert to lowercase
        text = re.sub(r'[^a-z0-9\s]', '', text)  # Remove special characters
        return text

def preprocess_order_data(df):
    df['product'] = df['product'].apply(detect_and_translate).apply(normalize_text) # applying translation & then normalization
    df['special_instructions'] = df['special_instructions'].apply(detect_and_translate).apply(normalize_text) # applying translation & then normalization

    return df

# Sample input
data = pd.DataFrame({
    'order_id': [1, 2, 3],
    'product': ['T-shirt', 'জিন্স', '衬衫'],
    'quantity': [1000, 500, 750],
    'special_instructions': ['Rush order', 'দ্রুত প্রয়োজন', 'Standard shipping']
})

# Preprocess the data
processed_data = preprocess_order_data(data)
print(processed_data)
