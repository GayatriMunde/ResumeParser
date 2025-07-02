import streamlit as st
from resume_matcher import ResumeMatcher
import tempfile
import os

st.set_page_config(page_title="Resume–JD Match", page_icon="📄")
st.title("📄 Resume–Job Match Evaluator")

jd_text = st.text_area("Paste the Job Description here", height=200)
uploaded_file = st.file_uploader("Upload a Resume (.docx)", type=["docx"])

if "result" not in st.session_state:
    st.session_state["result"] = None

if st.button("🔍 Evaluate Match", key="evaluate_button"):
    if not jd_text:
        st.warning("⚠️ Please paste the job description first.")
    elif not uploaded_file:
        st.warning("⚠️ Please upload a resume.")
    else:
        with st.spinner("Analyzing resume..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
                tmp.write(uploaded_file.read())
                resume_path = tmp.name

            matcher = ResumeMatcher(jd_text)
            matcher.load_resumes(os.path.dirname(resume_path))
            results = matcher.rank(top_n=1)

            if results:
                st.session_state["result"] = results[0]
            else:
                st.session_state["result"] = None
                st.error("❌ Could not parse or match the resume. Please check the format.")

# --- Render result ---
result = st.session_state["result"]
if result:
    st.success("✅ Match evaluation completed!")

    st.subheader("🔎 Match Result")
    st.markdown(f"**Match Score:** `{result['score']}%`")

    matched = result.get("matched_keywords", [])
    st.markdown(f"**Matched Keywords:** {', '.join(matched) if matched else 'None'}")

    st.markdown("**JD Skills (Matched):**")
    st.code(", ".join([kw for kw in matched if kw in jd_text.lower()]))

    st.markdown("**Resume Skills (Matched):**")
    st.code(", ".join([kw for kw in matched if kw in result["resume_data"].get("skills", [])]))

    st.markdown("---")
    st.subheader("📄 Resume Overview")
    st.json(result["resume_data"])

# os.remove(resume_path)
