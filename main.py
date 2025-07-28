import streamlit as st
import PyPDF2
import io
from openai import OpenAI
from dotenv import load_dotenv
from os import getenv

load_dotenv()

st.set_page_config(page_title="AI Resumer Analyzer", page_icon="📑" , layout="centered")
st.title("AI Resume Analyzer")
st.markdown("Upload your Resume and get AI-powered feedback!")

upload_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"] )
job_role = st.text_input("Enter the job role you are targetting (optional)")

analyze = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text+=page.extract_text()+"\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")
    
if analyze and upload_file:
    try:
        file_content = extract_text_from_file(upload_file)
        if not file_content.strip():
            st.error("File does not have any content..")
            st.stop()
        
        prompt =f"""Please analyze this resume and provide constructive feedback.
        Focus on following aspects:
        1. Content Clarity and impact
        2. Skills Presentation
        3. Experience description
        4. Specific Improvements for {job_role if job_role else 'general Job application'}

        Resume Content:
        {file_content}
        please provide your analysis in a clear , structured format with specific recommendations."""

        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"],base_url=st.secrets["OPENAI_API_BASE"])
        response = client.chat.completions.create(
            model=st.secrets["OPENAI_MODEL_NAME"],
            messages=[
                {"role":"system", "content":"You are an expert resume reviewer with years of experience in HR and recruitement"},
                {"role":"user","content":prompt}
                ],
            temperature=0.7,
            max_tokens=1000
        )
        st.markdown("### Analysis")
        st.markdown(response.choices[0].message.content)

    except Exception as e:
        st.error(f"An error occured: {str(e)}")
