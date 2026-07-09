from ai_engine.preprocessing import clean_text, remove_stopwords, lemmatize_text
from ai_engine.scorer import get_cosine_similarity, weighted_match, get_final_score
from ai_engine.llm_router import LLMRouter
from ai_engine.question_generator import QuestionGenerator

llm = LLMRouter()


def get_full_analysis(resume_text: str, jd_text: str):
    print("STEP 1: function called")

    # -----------------------------
    # 1. Preprocessing
    # -----------------------------
    resume = lemmatize_text(remove_stopwords(clean_text(resume_text)))
    jd = lemmatize_text(remove_stopwords(clean_text(jd_text)))
    print("STEP 2: preprocessing done")

    # -----------------------------
    # 2. Skills
    # -----------------------------
    required_skills = {
        "python": 3,
        "sql": 2,
        "machine learning": 4,
        "aws": 2,
        "deep learning": 4,
        "nlp": 3
    }

    # -----------------------------
    # 3. Scoring
    # -----------------------------
    cosine = get_cosine_similarity(resume, jd)

    matched, missing, match_percent = weighted_match(resume, required_skills)

    final_score = get_final_score(match_percent, cosine, True)

    scores = {
        "ats_score": round(final_score, 2),
        "cosine_score": round(cosine, 2),
        "skill_match_percent": round(match_percent, 2),
        "matched_skills": matched,
        "missing_skills": missing
    }

    print("STEP 3: scoring done", scores)

    #question generate
    qg = QuestionGenerator()
    questions = qg.generate_questions(resume_text, jd_text, missing)

    # -----------------------------
    # 4. LLM Insights
    # -----------------------------
    print("STEP 4: calling LLM")

    insights = llm.generate(resume_text, jd_text, scores)
    print("STEP Q: questions", questions)



    print("STEP 5: LLM response", insights)

    # -----------------------------
    # 5. Final Response
    # -----------------------------
    return {
        **scores,
        "insights": insights["data"],
        "llm_used": insights["provider"],
        "questions": questions["data"]
    }