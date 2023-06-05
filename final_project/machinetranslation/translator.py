"""
    Translation Module
"""

from deep_translator import MyMemoryTranslator
from deep_translator import GoogleTranslator

def english_to_french(english_text):
    """
    English to French Translator Function
    """
    french_text = GoogleTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    French to English Translator Function
    """
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
