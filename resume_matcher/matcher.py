# matcher.py

import os
from .parser import ResumeParser  # Import the module, not a class
from .sematic_matcher import SemanticMatcher


class ResumeMatcher:
    def __init__(self, jd_text):
        self.jd_text = jd_text
        self.semantic_model = SemanticMatcher()
        self.resumes = []
        self.ranked_results = []

    def load_resumes(self, directory):
        self.resumes = []
        print("📁 Scanning folder:", directory)

        for file in os.listdir(directory):
            if file.endswith(".docx"):
                full_path = os.path.join(directory, file)
                print(f"📝 Parsing: {file}")

                parser = ResumeParser()  # create an instance
                data = parser.parse_resume(full_path)
                blob = parser.build_resume_blob(data)

                semantic_score = self.semantic_model.get_similarity(self.jd_text, blob)
                matched_keywords = self.semantic_model.highlight_matching_keywords(self.jd_text, blob)

                data["semantic_score"] = round(semantic_score * 100, 1)
                data["matched_keywords"] = matched_keywords

                self.resumes.append({
                    "filename": file,
                    "resume_data": data,
                    "score": round(semantic_score * 100, 1)
                })

        print(f"✔️ Resumes loaded: {len(self.resumes)}")

    def rank(self, top_n=10):
        if not self.resumes:
            return []

        self.ranked_results = sorted(self.resumes, key=lambda x: x["score"], reverse=True)
        return self.ranked_results[:top_n]
