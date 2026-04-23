import streamlit as st
import pandas as pd
import tempfile, os
from parser import parse_resume
from matcher import get_match_score, get_skill_gap

st.set_page_config(page_title="AI Resume Screener", page_icon="📄", layout="wide")
st.title("AI Resume Screener")
st.markdown("Upload resumes and paste a job description to get ranked match scores.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Job Description")
    job_desc = st.text_area("Paste JD here", height=300,
        placeholder="e.g. We are looking for a Python developer with ML experience...")

with col2:
    st.subheader("Upload Resumes")
    uploaded = st.file_uploader("Upload PDF resumes",
        accept_multiple_files=True, type=["pdf"])

if st.button("Screen Resumes", type="primary"):
    if not job_desc or not uploaded:
        st.error("Please add a job description and upload at least one resume.")
    else:
        results = []
        with st.spinner("Analyzing resumes..."):
            for file in uploaded:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(file.read())
                    tmp_path = tmp.name
                resume_text = parse_resume(tmp_path)
                os.unlink(tmp_path)
                score = get_match_score(resume_text, job_desc)
                matched, missing = get_skill_gap(resume_text, job_desc)
                results.append({
                    "Candidate": file.name.replace(".pdf", ""),
                    "Match Score (%)": score,
                    "Matched Skills": ", ".join(matched),
                    "Missing Skills": ", ".join(missing)
                })

        df = pd.DataFrame(results).sort_values("Match Score (%)", ascending=False)
        df.index = range(1, len(df) + 1)
        st.subheader("Results")
        st.dataframe(df, width='stretch')
        st.bar_chart(df.set_index("Candidate")["Match Score (%)"])
        csv = df.to_csv(index=False)
        st.download_button("Download Results as CSV", csv, "results.csv", "text/csv")