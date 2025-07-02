# skill_matcher.py

import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Doc, Span
from spacy.language import Language

@Language.factory("skill_matcher")
def create_skill_matcher(nlp, name):
    return SkillMatcher(nlp)

class SkillMatcher:
    def __init__(self, nlp):
        self.matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
        self.skills = self._load_skills()
        patterns = [nlp.make_doc(skill) for skill in self.skills]
        self.matcher.add("SKILLS", patterns)

        # Register custom extension
        if not Doc.has_extension("skills"):
            Doc.set_extension("skills", default=[])

    def __call__(self, doc):
        matches = self.matcher(doc)
        spans = [Span(doc, start, end, label="SKILL") for _, start, end in matches]
        doc._.skills = list({span.text for span in spans})  # deduplicated
        return doc

    def _load_skills(self):
        return [
            "Python", "Java", "SQL", "Flask", "Django", "REST APIs",
            "Linux", "Windows", "MacOS", "Docker", "Kubernetes",
            "Git", "CI/CD", "Communication", "Troubleshooting",
            "Integration", "Debugging", "PostgreSQL", "AWS", "Android", "iOS"
        ]
