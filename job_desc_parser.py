import re
import string

class JobDescriptionParser:
    def __init__(self, jd_text):
        self.raw_text = jd_text
        self.cleaned_text = ""
        self.required_skills = []
        self.required_experience = None
        self.education_requirements = []
        self.job_title = None

    def clean_text(self):
        """
        Preprocess the JD text:
        - Lowercase
        - Remove punctuation
        - Normalize whitespace
        """
        text = self.raw_text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        self.cleaned_text = re.sub(r'\s+', ' ', text).strip()

    def extract_job_title(self):
        """
        Extract job title from the top few lines of the raw text.
        """
        lines = self.raw_text.strip().split("\n")
        for line in lines[:5]:  # only look at top few lines
            if "engineer" in line.lower() or "developer" in line.lower() or "manager" in line.lower():
                self.job_title = line.strip()
                break

    def extract_required_skills(self, skill_vocab):
        """
        Match known skills against cleaned JD text.
        """
        matched_skills = []
        for skill in skill_vocab:
            pattern = r'\b' + re.escape(skill.lower()) + r'\b'
            if re.search(pattern, self.cleaned_text):
                matched_skills.append(skill)
        self.required_skills = matched_skills

    def extract_experience_level(self):
        """
        Extract required years of experience using regex.
        """
        match = re.search(r'(\d+)\+?\s+(years|yrs).*experience', self.cleaned_text)
        if match:
            self.required_experience = int(match.group(1))

    def extract_education_requirements(self):
        """
        Look for common degree keywords in the JD.
        """
        degrees = ["bachelor", "master", "phd", "b.tech", "m.tech", "mba", "b.sc", "m.sc"]
        found = []
        for degree in degrees:
            if degree in self.cleaned_text:
                found.append(degree.title())
        self.education_requirements = list(set(found))

    def get_structured_output(self):
        return {
            "job_title": self.job_title,
            "required_skills": self.required_skills,
            "required_experience": self.required_experience,
            "education_requirements": self.education_requirements
        }

    def parse(self, skill_vocab):
        self.clean_text()
        self.extract_job_title()
        self.extract_required_skills(skill_vocab)
        self.extract_experience_level()
        self.extract_education_requirements()
        return self.get_structured_output()
