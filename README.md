# 📄 ResumeParser – ML-Powered Resume Matching System

**ResumeParser** is an end-to-end intelligent resume screening tool that helps recruiters rank candidate resumes based on semantic relevance to a job description. It leverages NLP and machine learning to extract, parse, and match resumes—going beyond basic keyword filtering to true contextual understanding.

---

## 🚀 Features

- ✅ Extracts structured data (skills, education, experience) from `.docx` resumes
- 🧠 Uses [Sentence-BERT](https://www.sbert.net/) for semantic JD–resume matching
- 🔍 Highlights matched keywords from resumes and JD
- 📊 Classifies candidates into `shortlist`, `considered`, and `unconsidered` buckets
- 🌐 Streamlit UI for evaluating match score between a JD and uploaded resume
- 🧩 Modular design to build a pluggable API for Workday or ATS integration

---

## 🧰 Tech Stack

- Python 3.8+
- [spaCy](https://spacy.io/)
- [sentence-transformers](https://www.sbert.net/)
- [Streamlit](https://streamlit.io/)
- [python-docx](https://python-docx.readthedocs.io/)
- [scikit-learn](https://scikit-learn.org/)
- [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy)

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ResumeParser.git
cd ResumeParser
```

### 2. Create and activate virtual environment (recommended)

```bash
python -m venv env
# Windows
env\Scripts\activate
# macOS/Linux
source env/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
python -m nltk.downloader punkt
python -m spacy download en_core_web_sm
```

### 4. Run the Streamlit app
```bash
streamlit run app.py
```
