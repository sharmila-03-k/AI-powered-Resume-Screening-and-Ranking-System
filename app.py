import streamlit as st
import os
from resume_parser import extract_skills
from ranker import rank_resumes

# Load job description
job_desc = open("job_description.txt", "r").read()

# Title
st.title("AI-powered Resume Screening & Ranking")

# Upload resumes
uploaded_files = st.file_uploader("Upload Resumes", accept_multiple_files=True, type=['txt'])

if uploaded_files:
    resume_texts = []
    filenames = []
    for file in uploaded_files:
        text = file.read().decode("utf-8")
        resume_texts.append(text)
        filenames.append(file.name)

    # Rank resumes
    results = rank_resumes(resume_texts, job_desc)

    st.subheader("Ranked Resumes")
    for rank, (idx, score) in enumerate(results, start=1):
        st.write(f"**#{rank}: {filenames[idx]}** - Score: {score[0]:.2f}")
        st.text_area("Resume Snippet", resume_texts[idx][:500], height=150)
