import streamlit as st
from utils import extract_text, calculate_score
import pandas as pd

st.set_page_config(page_title="ATS Resume Screener")

st.title("ATS Resume Screener")

job_desc = st.text_area("Paste Job Description")

uploaded_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

if uploaded_files and job_desc:
    results = []

    for file in uploaded_files:
        text = extract_text(file)
        score = calculate_score(text, job_desc)

        results.append((file.name, score))

    results.sort(key=lambda x: x[1], reverse=True)

    st.subheader("Results")

    for name, score in results:
        st.write(f"**{name}** — Match Score: {score}%")

    df = pd.DataFrame(results, columns=["Resume", "Match Score"])
    st.dataframe(df)

    st.bar_chart(df.set_index("Resume"))

#run the app with: python -m streamlit run app.py in the terminal.