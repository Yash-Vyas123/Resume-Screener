from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from preprocessor import clean_text, extract_keywords

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_match_score(resume_text, job_desc_text):
    clean_resume = clean_text(resume_text)
    clean_jd = clean_text(job_desc_text)
    embeddings = model.encode([clean_resume, clean_jd])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(float(score) * 100, 2)

def get_skill_gap(resume_text, job_desc_text):
    resume_kw = set(extract_keywords(resume_text))
    jd_kw = set(extract_keywords(job_desc_text))
    missing = jd_kw - resume_kw
    matched = jd_kw & resume_kw
    return list(matched)[:10], list(missing)[:10]