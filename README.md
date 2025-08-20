# Resume-to-Job Matcher AI App

## Overview

This is a smart, recruiter-style Streamlit web app that analyzes how well a resume matches a job description using AI-powered language models. It extracts and compares key skills and keywords using embeddings and NLP techniques to generate an overall match score and explain key overlaps and gaps.

## Features

- Paste a **resume** and a **job description** directly into the interface
- Instant AI-powered similarity scoring using **sentence-transformers**
- Interactive **keyword overlap visualizations** (skills match)
- Clear explanations of which keywords are aligned or missing
- Clean and professional user interface

## Why This Project?

Matching resumes to job descriptions is a crucial step in the hiring process. This tool simulates the backend of modern ATS (Applicant Tracking Systems), giving jobseekers or hiring teams an intelligent way to assess compatibility before submitting or reviewing resumes.

## Technologies Used

- **Streamlit** – Frontend web app
- **Sentence-Transformers** – Semantic similarity scoring using pretrained language models
- **Scikit-learn** – Cosine similarity calculation
- **NLTK** – Basic NLP cleaning and keyword extraction
- **Pandas / NumPy** – Data wrangling and matching logic

## How It Works

1. User pastes in their resume and a job description.
2. The app encodes both texts using a BERT-based sentence transformer.
3. It computes a **similarity score (0–100%)**.
4. It extracts important keywords and highlights:
   - Skills found in both resume and job description
   - Missing keywords in the resume

## Deployment

The app is deployed using Streamlit Cloud and can be accessed via the following link:

[Insert your deployment URL here once live]

---

## Future Improvements

- PDF and DOCX resume upload support
- Contextual scoring with experience-level weighting
- ATS-optimized resume feedback
- Downloadable match report (PDF)
- User authentication and history tracking

---

## License

MIT License. Feel free to fork, customize, and deploy your own version.
