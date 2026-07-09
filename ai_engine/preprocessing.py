# PREPROCESSING
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from nltk.stem import WordNetLemmatizer
import re

lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-z0-9. ]', '', text)
    return text.strip()

def remove_stopwords(text):
    words = text.split()
    return " ".join([w for w in words if w not in ENGLISH_STOP_WORDS])

def lemmatize_text(text):
    words = text.split()
    return " ".join([lemmatizer.lemmatize(w) for w in words])