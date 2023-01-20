from pathlib import Path

import streamlit as st
from PIL import Image

# ---------- PATH SETTINGS -----------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"MyCv.pdf"
profile_pic = current_dir/"assets"/"MyProfile.png"


# ----------- GENERAL SETTINGS ----------
PAGE_TITLE = "Digital CV By Using Python | Arghya Samanta"
PAGE_ICON = ":wave:"    # emoji name, lets try for "random"
NAME = "Arghya Samanta"
DESCRIPTION = """
Computer Science Engineer(Fresher), Pursuing B.Tech from CIEM, Tollygunge Under MAKAUT
"""
EMAIL = "arghya.samanta62@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/arghya--samanta/",
    "GitHub": "https://github.com/ARG50",
}

PROJECTS = {
    "🏆 Desktop Application ---"
    " An app, using Java & Swing, can performs encryption and decryption operation on a file.":
        "https://github.com/ARG50/Encryptor-App",
    "🏆 Digital Cv --- A digital Cv, using python & css, through a webpage. ":
        "https://github.com/ARG50/My-Virtual-CV"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Hi There! This is My Digital Cv.")


# ----------- LOAD CSS, PDF & PROFILE PIC ---------------
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)



# ---------------- PROFILE SECTION -------------------
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=240)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="applications/octet-stream"
    )
    st.write("📧",EMAIL)


