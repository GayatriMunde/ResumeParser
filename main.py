import os
from resume_matcher import ResumeMatcher

jd_text = """We are hiring a backend engineer with experience in Flask, Python, and AWS.
Candidate must have strong communication skills and experience with Git, CI/CD pipelines, and Docker.
"""

matcher = ResumeMatcher(jd_text)
matcher.load_resumes("Resumes")
print("✔️ Loaded resumes:", [r["filename"] for r in matcher.ranked_results])


ranked = matcher.rank(top_n=50)

if not ranked:
    print("⚠️ No resumes matched or found.")

for res in ranked:
    print(f"\n✅ {res['filename']} — Match: {res['score']}%")
    print("Matched Skills:", res["resume_data"].get("matched_keywords", []))
