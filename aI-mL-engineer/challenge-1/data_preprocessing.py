import pandas as pd
import langid
import re
from deep_translator import GoogleTranslator


class OrderDataProcessor:
    def __init__(self):
        self.translator = GoogleTranslator()
    
    def detectLanguage(self, text):
        if pd.isna(text) or text.strip() == "":
            return None, text
        try:
            lang, _ = langid.classify(text)
            return lang, text
        except Exception as e:
            print(f"Language detection error: {e}")
            return None, text

    def translateToEnglish(self, lang, text):
        if lang and lang != 'en':
            try:
                return self.translator.translate(text, source=lang, target='en')
            except Exception as e:
                print(f"Translation error: {e}")
        return text

    def normalizeText(self, text):
        if pd.isna(text):
            return ""
        text = text.lower() 
        text = re.sub(r'[^a-z0-9\s]', '', text)  # Remove special characters
        return text

    def processText(self, text):
        lang, detectedText = self.detectLanguage(text) # Step 1: Detect language
        translatedText = self.translateToEnglish(lang, detectedText) # Step 2: Translate to English if needed
        normalizedText = self.normalizeText(translatedText) # Step 3: Normalize the text
        return normalizedText

    def preprocessOrderData(self, df):
        for column in df.columns:
            if df[column].dtype == object:  # Apply to text columns
                df[column] = df[column].apply(self.processText)
        return df
    

data = pd.DataFrame({
    'order_id': [1, 2, 3],
    'product': ['T-shirt', 'জিন্স', '衬衫'],
    'quantity': [1000, 500, 750],
    'special_instructions': ['Rush order', 'দ্রুত প্রয়োজন', 'Standard shipping']
})

processor = OrderDataProcessor()
preprocessedData = processor.preprocessOrderData(data)
print(preprocessedData)
