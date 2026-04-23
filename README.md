# AI Resume Screener

An intelligent resume screening system that matches resumes 
against job descriptions using BERT embeddings and NLP.

## Features
- Upload multiple PDF resumes at once
- Paste any job description
- Get match score (0-100%) for each candidate
- View matched and missing skills
- Download results as CSV

## Tech Stack
- Python
- Streamlit (Web UI)
- sentence-transformers / BERT (Semantic Matching)
- spaCy (NLP Preprocessing)
- pdfminer.six (PDF Text Extraction)
- scikit-learn (Cosine Similarity)
- pandas (Data Handling)

## How It Works
1. Resume PDF is parsed using pdfminer
2. Text is cleaned and lemmatized using spaCy
3. BERT model converts text to 384-dimensional vectors
4. Cosine similarity gives match percentage
5. Results displayed in Streamlit dashboard

## Run Locally
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
```
