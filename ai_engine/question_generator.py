from ai_engine.llm_router import LLMRouter

class QuestionGenerator:

    def __init__(self):
        self.llm = LLMRouter()

    def generate_questions(self, resume_text, jd_text, missing_skills):

        prompt = f"""
You are a senior software engineer and interviewer.

Generate high-quality interview questions based on:

1. Resume
2. Job Description
3. Missing Skills

----------------------------------------

Resume:
{resume_text}

Job Description:
{jd_text}

Missing Skills:
{missing_skills}

----------------------------------------

INSTRUCTIONS:

- Generate 8-10 interview questions
- Mix of:
  - Technical (DSA, backend, system design)
  - Project-based (from resume)
  - Skill-gap based (from missing skills)
- Questions should be:
  - Practical
  - Real interview level
  - Not generic

----------------------------------------

OUTPUT FORMAT (STRICT JSON):

{{
  "questions": [
    "Question 1",
    "Question 2"
  ]
}}
"""

        result = self.llm.generate(resume_text, jd_text, {"type": "questions", "prompt": prompt})

        return result