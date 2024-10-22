import base64
from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"
linkedin_logo  = current_dir / "assets" / "linkedin-original.svg"
github_logo  = current_dir / "assets" / "github.svg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Chong Jack Pang"
PAGE_ICON = ":wave:"
NAME = "Chong Jack Pang"
DESCRIPTION = """
AI Fresh Graduate, Data & AI enthusiast.
"""
EMAIL = "jpchong24@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/jack-pang-chong-520a0226b/",
    "GitHub": "https://github.com/cipe5555",
}
PROJECTS = {
    "🏆 Final Year Project - Job Recommendation System with Content-Based Filtering Method": "https://github.com/cipe5555/job-recommender",
    "🏆 Timetable Converter - Converting university timetable to calendar event with data engineering approach": "https://github.com/cipe5555/APU-Timetable-to-Google-Calendar",
    "🏆 1st Runner-up in APU-AWS DeepRacer Competition 2023 - Autonomous car racing with Reinforcement Learning (RL)": "https://www.digitalnewsasia.com/business/apu-aws-deepracer-competition-2023-showcases-future-machine-learning-and-data-science",
    "🏆 Automated Scene Description with Image Processing": "https://github.com/cipe5555/imaging-and-special-effect",
    "🏆 Glove Defect Detection System - Implementing computer vision for quality control": "https://github.com/cipe5555/image-processing-and-pattern-recognition",
    "🏆 Text Analysis and Twitter Sentiment Analysis - Using NLP for sentiment extraction": "https://github.com/cipe5555/text-analysis-and-sentiment-analysis",
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
    st.markdown(f"<h1 style='font-size: 42px;'>{NAME}</h1>", unsafe_allow_html=True)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


def render_svg(svg_path: Path, width: int = 20):
    with open(svg_path, "r") as f:
        svg = f.read()
    b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
    html = f'<img src="data:image/svg+xml;base64,{b64}" width="{width}" style="vertical-align:middle; margin-right:10px;" />'
    return html

# SOCIAL LINKS with SVG logos and links on the same line
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    if platform == "LinkedIn":
        with cols[index]:
            linkedin_svg = render_svg(linkedin_logo)
            st.markdown(f"{linkedin_svg} [**{platform}**]({link})", unsafe_allow_html=True)
    elif platform == "GitHub":
        with cols[index]:
            github_svg = render_svg(github_logo)
            st.markdown(f"{github_svg} [**{platform}**]({link})", unsafe_allow_html=True)






# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Hands-on experience with machine learning frameworks such as PyTorch and TensorFlow, applied to text sentiment detection, heart failure detection, and diabetes detection
- ✔️ Experienced in scraping, data extraction, and pipeline development using Python libraries like BeautifulSoup and Selenium
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Developed skills through project-based learning
- ✔️ Experienced in ETL (Extract, Transform, Load) processes and data warehousing using Snowflake
- ✔️ Familiar with workflow orchestration tools like Airflow, Dagster, and Prefect for managing and automating complex data pipelines
- ✔️ Familiar with project management tool like Jira
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 **Programming**: Python, Java, C, C++, SQL, Kotlin, Matlab
- 🛠️ **Data & AI Frameworks**: PyTorch, TensorFlow, Streamlit, Scikit-learn
- 📊 **Data Visulization**: PowerBI, MS Excel, Matplotlib, Seaborn
- 📚 **Modeling**: Logistic Regression, Linear Regression, Decision Trees, Random Forest, k-Nearest Neighbors (k-NN)
- 🗄️ **Databases**: Postgres, MongoDB, MySQL, BigQuery
- 🔍 **Data Engineering**: ETL Pipelines, Web Scraping, Data Cleaning
- 🔄 **ETL Tools**: Snowflake, Airflow, Dagster, Prefect
- 📅 **Project Management**: Jira
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



# --- LANGUAGES ---
st.write('\n')
st.subheader("Languages")
st.write(
    """
- 🇺🇸 **English**: Proficient
- 🇲🇾 **Malay**: Proficient
- 🇨🇳 **Mandarin**: Proficient
"""
)
