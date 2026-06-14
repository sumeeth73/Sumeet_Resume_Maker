import streamlit as st
from fpdf import FPDF
import tempfile

st.set_page_config(page_title="Resume Maker", layout="centered")

st.title("📄 Resume Maker")

# User Inputs
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
role = st.text_input("Professional Title")

summary = st.text_area("Professional Summary")

skills = st.text_area(
    "Skills (comma separated)",
    placeholder="Python, SQL, Machine Learning"
)

education = st.text_area(
    "Education",
    placeholder="B.Tech in Computer Science - XYZ University"
)

experience = st.text_area(
    "Work Experience",
    placeholder="Software Engineer at ABC Company (2022-Present)"
)

projects = st.text_area(
    "Projects",
    placeholder="Resume Generator using Streamlit"
)


def create_resume_pdf():
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, name, ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, f"{role}", ln=True)
    pdf.cell(0, 8, f"Email: {email}", ln=True)
    pdf.cell(0, 8, f"Phone: {phone}", ln=True)

    pdf.ln(5)

    # Summary
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Professional Summary", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, summary)

    # Skills
    pdf.ln(2)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Skills", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, skills)

    # Education
    pdf.ln(2)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Education", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, education)

    # Experience
    pdf.ln(2)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Experience", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, experience)

    # Projects
    pdf.ln(2)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Projects", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, projects)

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp_file.name)

    with open(temp_file.name, "rb") as f:
        pdf_bytes = f.read()

    return pdf_bytes


if st.button("Generate Resume PDF"):
    if not name:
        st.error("Please enter your name.")
    else:
        pdf_data = create_resume_pdf()

        st.success("Resume generated successfully!")

        st.download_button(
            label="⬇ Download Resume PDF",
            data=pdf_data,
            file_name=f"{name.replace(' ', '_')}_Resume.pdf",
            mime="application/pdf",
        )