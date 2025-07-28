
# 📑 AI Resume Analyzer

AI Resume Analyzer is a Streamlit-based web app that provides AI-powered feedback on your resume. Simply upload your PDF or TXT resume, and get personalized, structured analysis to help you improve it for your targeted job role.

🔗 **Live App**: [https://ai-resume-analyzer-new.streamlit.app/](https://ai-resume-analyzer-new.streamlit.app/)

---

## 🚀 Features

- 📄 Upload your resume (PDF or TXT)
- 🎯 Optionally specify the job role you're applying for
- 🤖 Get AI-generated feedback on:
  - Content clarity and impact
  - Skills presentation
  - Experience description
  - Specific recommendations for improvements

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) for UI
- [OpenAI API](https://platform.openai.com/) for resume analysis
- [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF parsing
- [dotenv](https://pypi.org/project/python-dotenv/) for environment variable management

---

## 🔐 Environment Variables

For local development, add a `.env` file or use `.streamlit/secrets.toml` with the following keys:

```toml
OPENAI_API_KEY = "your-openai-api-key"
OPENAI_API_BASE = "https://api.openai.com/v1"
OPENAI_MODEL_NAME = "gpt-3.5-turbo"
````

---

## ▶️ Run Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/ai-resume-analyzer.git
   cd ai-resume-analyzer
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

---

