import json
from resume_parser import ResumeParser
from semantic_matcher import SemanticMatcher

sample_jd = """ 
We are looking for a skilled Backend Software Engineer to join our team.
Design APIs using Flask, work on scalable systems, and deploy on AWS.
2+ years experience preferred. Bachelor's or Master's required.
"""

parser = ResumeParser()
semantic_model = SemanticMatcher()

resumes_path = "C:/Users/g37ti/IdeaProjects/ResumeParser/Resumes"
parsed_resumes = parser.parse_directory(resumes_path)

ranked = []

# Score resumes
for filename, resume_data in parsed_resumes.items():
    resume_blob = parser.build_resume_blob(resume_data)
    similarity = semantic_model.get_similarity(sample_jd, resume_blob)
    highlights = semantic_model.highlight_matching_keywords(sample_jd, resume_blob)

    resume_data["semantic_score"] = round(similarity * 100, 1)
    resume_data["matched_keywords"] = highlights
    ranked.append((filename, resume_data, resume_data["semantic_score"]))

# Sort by score descending
ranked.sort(key=lambda x: x[2], reverse=True)

# Categorize candidates
candidate_rank = {
    "shortlist": [],
    "considered": [],
    "unconsidered": []
}

print("\nRanked Resumes (Semantic Match Only):")
for filename, data, score in ranked:
    print(f"\n{filename} — Semantic Match Score: {score}%")

    if score > 80:
        candidate_rank["shortlist"].append({"filename": filename, "score": score})
    elif score > 40:
        candidate_rank["considered"].append({"filename": filename, "score": score})
    else:
        candidate_rank["unconsidered"].append({"filename": filename, "score": score})

# Output categorized rankings
print("\nCandidate Ranking Summary:")
print(json.dumps(candidate_rank, indent=4))
