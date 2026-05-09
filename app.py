import streamlit as st

from extract_text import (
    extract_text_from_docx,
    extract_text_from_pdf
)

from preprocess import preprocess_text

from skill_extraction import extract_skills

from matcher import calculate_similarity

from visualization import plot_skill_match



st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)



st.title("📄 Resume Analyzer using NLP")

st.markdown(
    "Analyze resumes and match them with job descriptions using Natural Language Processing."
)



# SIDEBAR

st.sidebar.title("About")

st.sidebar.info(
    "This application extracts skills from resumes and compares them with job descriptions using NLP techniques."
)



# MAIN LAYOUT

col1, col2 = st.columns(2)



with col1:

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["docx", "pdf"]
    )



with col2:

    job_description = st.text_area(
        "Paste Job Description",
        height=250
    )



if uploaded_file is not None and job_description:


    # SAVE TEMP FILE

    if uploaded_file.name.endswith(".docx"):

        with open("temp_resume.docx", "wb") as f:
            f.write(uploaded_file.getbuffer())

        resume_text = extract_text_from_docx(
            "temp_resume.docx"
        )


    elif uploaded_file.name.endswith(".pdf"):

        with open("temp_resume.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        resume_text = extract_text_from_pdf(
            "temp_resume.pdf"
        )


    # PREPROCESSING

    resume_cleaned = preprocess_text(resume_text)

    job_cleaned = preprocess_text(job_description)


    # SKILL EXTRACTION

    resume_skills = extract_skills(resume_cleaned)

    job_skills = extract_skills(job_cleaned)


    # SKILL MATCHING

    matched_skills = set(resume_skills).intersection(
        set(job_skills)
    )


    if len(job_skills) > 0:

        skill_score = (
            len(matched_skills) / len(job_skills)
        ) * 100

    else:

        skill_score = 0


    # TF-IDF SIMILARITY

    similarity_score = calculate_similarity(
        resume_cleaned,
        job_cleaned
    )


    # RESULTS

    st.divider()

    st.subheader("📊 Matching Results")


    c1, c2 = st.columns(2)


    with c1:

        st.metric(
            "Skill Matching Score",
            f"{skill_score:.2f}%"
        )

        st.progress(skill_score / 100)


    with c2:

        st.metric(
            "TF-IDF Similarity",
            f"{similarity_score:.2f}%"
        )

        st.progress(similarity_score / 100)


    st.divider()


    # SKILLS DISPLAY

    a1, a2, a3 = st.columns(3)


    with a1:

        st.subheader("✅ Resume Skills")

        st.write(resume_skills)


    with a2:

        st.subheader("📌 Job Skills")

        st.write(job_skills)


    with a3:

        st.subheader("🎯 Matched Skills")

        st.write(list(matched_skills))


    # VISUALIZATION

    st.divider()

    st.subheader("📈 Skill Match Visualization")

    fig = plot_skill_match(
        resume_skills,
        matched_skills
    )

    st.pyplot(fig)