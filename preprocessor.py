import spacy
import re

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower().strip()
    doc = nlp(text)
    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop and token.is_alpha and len(token) > 2
    ]
    return " ".join(tokens)

def extract_keywords(text, top_n=20):
    doc = nlp(text)
    keywords = [
        token.lemma_.lower()
        for token in doc
        if not token.is_stop and token.is_alpha and len(token) > 3
    ]
    return list(set(keywords))[:top_n]