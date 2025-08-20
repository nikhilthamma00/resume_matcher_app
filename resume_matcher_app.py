import streamlit as st
import re
import string
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --------------------- CONFIG ---------------------
st.set_page_config(page_title="Resume-to-Job Matcher", page_icon="🧠", layout="wide")

# --------------------- HEADER ---------------------
st.markdown("<h1 style='text-align: center;'>🧠 Resume-to-Job Matcher</h1>", unsafe_allow_html=True)
st.markdown("---")

# --------------------- INPUT SECTION ---------------------
col1, col2 = st.columns(2)

with col1:
    resume_text = st.text_area("📄 Paste Your Resume", height=300, placeholder="Paste your resume here...")

with col2:
    job_text = st.text_area("💼 Paste Job Description", height=300, placeholder="Paste the job description here...")

# --------------------- HELPER FUNCTIONS ---------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def extract_keywords(text):
    stopwords = set([
        'and', 'or', 'with', 'the', 'a', 'an', 'to', 'of', 'in', 'on', 'for',
        'by', 'is', 'are', 'as', 'at', 'this', 'that', 'from', 'be'
    ])
    words = re.findall(r'\b\w+\b', text.lower())
    return set([w for w in words if w not in stopwords and len(w) > 2])

# --------------------- SCAN BUTTON ---------------------
if st.button("🔍 Scan Resume for Match"):
    if not resume_text or not job_text:
        st.warning("⚠️ Please paste both your resume and the job description.")
    else:
        cleaned_resume = clean_text(resume_text)
        cleaned_job = clean_text(job_text)

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([cleaned_resume, cleaned_job])
        score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        match_score = int(score * 100)

        st.markdown("---")
        st.markdown("## 📊 Match Score")
        st.markdown(f"<h2 style='text-align:center; color:#4CAF50'>{match_score}% Match</h2>", unsafe_allow_html=True)
        st.progress(match_score)

        if match_score >= 80:
            st.success("✅ Great fit! Your resume aligns well with the job description.")
        elif match_score >= 60:
            st.warning("⚠️ Decent fit. Consider adding missing keywords from the job description.")
        else:
            st.error("❌ Low match. Tailor your resume more carefully to this job.")

        # Keyword Analysis
        resume_keywords = extract_keywords(resume_text)
        job_keywords = extract_keywords(job_text)

        matched_keywords = resume_keywords & job_keywords
        missing_keywords = job_keywords - resume_keywords

        st.markdown("---")
        st.markdown("### 🧠 Matched Keywords")
        if matched_keywords:
            st.markdown(" ".join([f"<span style='background-color:#d4edda;color:#155724;padding:5px 10px;margin:5px;border-radius:20px;display:inline-block'>{kw}</span>" for kw in matched_keywords]), unsafe_allow_html=True)
        else:
            st.write("No overlaps found.")

        st.markdown("### 🧩 Missing Keywords (Consider Adding)")
        if missing_keywords:
            st.markdown(" ".join([f"<span style='background-color:#f8d7da;color:#721c24;padding:5px 10px;margin:5px;border-radius:20px;display:inline-block'>{kw}</span>" for kw in missing_keywords]), unsafe_allow_html=True)
        else:
            st.write("No major keywords missing!")

# --------------------- SIDEBAR ---------------------
st.sidebar.title("🔍 About This App")
st.sidebar.info("""
This AI-powered matcher compares your resume with a job description to provide:
- A match score
- Matched & missing keywords
- Resume optimization guidance

🚀 Tip: Tailor your resume to include more job-specific terms!
""")
