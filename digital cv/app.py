from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | portfolio"
PAGE_ICON = ":wave:"
NAME = "Fatima Ezzahra FAOUZI"
DESCRIPTION = """
A Graphic Designer and a Web Developer
"""
EMAIL = "fatimaezzahra.fa1@gmail.com"
SOCIAL_MEDIA = {
    "GitHub": "https://github.com",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)








# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


#--- ABOUT ME ---
st.write('\n')
st.subheader("About Me")
st.write(
    """
I am a Graphic Designer & a Web Developer Student.
I am passionate about anything that has to do with programming, Digital Design & Art
"""
)




# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Strong hands on knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, Html & Css
- 📊 Data Visulization: MS Excel
"""
)


# --- EDUCATION ---
st.write('\n')
st.subheader("EDUCATION")
st.write("---")

# --- EDU 1
st.write("🚧", "**Multimedia Developer | eWA Digital School**")
st.write("10/2022 - Present")
st.write(
    """
- ► learning the basics of programming & coding: algorithme, python, Html & Css, Unix
- ► learning different design softwares: Photoshop, Adobe illustrator
"""
)

# --- EDU 2
st.write('\n')
st.write("🚧", "**Bachelor in English Studies | Ibn Zohr University**")
st.write("07/2017 ")
st.write(
    """
- ► Studied English Linguistics with a basic knowledge of language science & Translation
"""
)

