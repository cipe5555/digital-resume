from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Chong Jack Pang"
PAGE_ICON = ":wave:"
NAME = "Chong Jack Pang"
DESCRIPTION = """
AI Fresh Graduted, Data & AI enthusiast.
"""
EMAIL = "jpchong24@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/jack-pang-chong-520a0226b/",
    "GitHub": "https://github.com/cipe5555",
}
PROJECTS = {
    "🏆 Timetable Converter - Converting university timetable to calendar event with data engineering approach": "https://github.com/cipe5555/APU-Timetable-to-Google-Calendar",
    "🏆 1st Runner-up in APU-AWS DeepRacer Competition 2023 - Autonomous car racing with Reinforcement Learning (RL)": "https://www.digitalnewsasia.com/business/apu-aws-deepracer-competition-2023-showcases-future-machine-learning-and-data-science",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 7 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Science Intern | Hiredly**")
st.write("08/2023 - 11/2023")
st.write(
    """
- ► Performed ETL processes, handling and integrating 500,000+ data points to ensure efficient data management.
- ► Designed and implemented automated task scheduling, reducing manual work by 30%, and developed 10+ automation scripts for routine tasks.
- ► Research on developing 2 APIs for ML/Data Ops purposes.
- ► Optimized the job recommendation system, resulting in a 5% improvement in matching accuracy than previous version and increased user engagement by 10%.
- ► Research and utilize LLM models to build AI-powered virtual interviewer.
"""
)




# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
