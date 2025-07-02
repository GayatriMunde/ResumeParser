from sentence_transformers import SentenceTransformer, util
from spacy.lang.en.stop_words import STOP_WORDS
import spacy

class SemanticMatcher:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def get_similarity(self, jd_text, resume_text):
        jd_vec = self.model.encode(jd_text, convert_to_tensor=True)
        res_vec = self.model.encode(resume_text, convert_to_tensor=True)
        return util.cos_sim(res_vec, jd_vec).item()

    def highlight_matching_keywords(self, jd_text, resume_text):
        jd_tokens = [token.text.lower() for token in self.nlp(jd_text) if not token.is_stop and token.is_alpha]
        resume_tokens = [token.text.lower() for token in self.nlp(resume_text) if not token.is_stop and token.is_alpha]

        jd_set = set(jd_tokens)
        resume_set = set(resume_tokens)

        matched_keywords = list(jd_set & resume_set)
        return matched_keywords
