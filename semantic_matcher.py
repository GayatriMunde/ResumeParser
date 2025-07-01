from sentence_transformers import SentenceTransformer, util

class SemanticMatcher:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def get_similarity(self, jd_text, resume_text):
        jd_embedding = self.model.encode(jd_text, convert_to_tensor=True)
        resume_embedding = self.model.encode(resume_text, convert_to_tensor=True)
        similarity = util.cos_sim(resume_embedding, jd_embedding).item()
        return round(similarity, 4)

    def highlight_matching_keywords(self, jd_text, resume_text, top_n=5):
        jd_words = list(set(jd_text.lower().split()))
        resume_words = list(set(resume_text.lower().split()))
        matches = [word for word in jd_words if word in resume_words and len(word) > 3]
        return matches[:top_n]
