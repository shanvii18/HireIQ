from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def weighted_match(resume_text, required_skills):
    total_weight = sum(required_skills.values())
    matched_weight = 0
    found_skills, missing_skills = [], []

    resume_text = resume_text.lower()

    for skill, weight in required_skills.items():
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'

        if re.search(pattern, resume_text):
            matched_weight += weight
            found_skills.append(skill)
        else:
            missing_skills.append(skill)

    if total_weight == 0:
        return [], [], 0.0

    match_percentage = (matched_weight / total_weight) * 100
    return found_skills, missing_skills, round(match_percentage, 2)


def get_cosine_similarity(resume_text, jd_text):
    if not jd_text or not jd_text.strip():
        return 0.0

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])

    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(score * 100, 2)


def get_final_score(match_percent, cosine_score, has_jd=True):
    if has_jd:
        return round((match_percent * 0.6) + (cosine_score * 0.4), 2)
    return match_percent