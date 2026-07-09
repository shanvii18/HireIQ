import os
from ai_engine.llm_analyzer_openai import OpenAIAnalyzer
from ai_engine.llm_analyzer_groq import GroqAnalyzer

class LLMRouter:

    def __init__(self):
        self.provider = os.getenv("LLM_PROVIDER", "groq")
        self.openai = OpenAIAnalyzer()
        self.groq = GroqAnalyzer()

    def generate(self, resume_text, jd_text, payload):

    # 🔥 CHECK: custom prompt (for questions)
        is_custom = isinstance(payload, dict) and payload.get("type") == "questions"

    # -----------------------------
    # OPENAI
    # -----------------------------
        if self.provider == "openai":
            try:
                if is_custom:
                    result = self.openai.generate_custom(payload["prompt"])
                else:
                    result = self.openai.generate_insights(resume_text, jd_text, payload)

                return {"provider": "openai", "data": result}

            except Exception as e:
                print("❌ OpenAI ERROR:", str(e))

    # -----------------------------
    # GROQ
    # -----------------------------
        if self.provider == "groq":
            try:
                if is_custom:
                    result = self.groq.generate_custom(payload["prompt"])
                else:
                    result = self.groq.generate_insights(resume_text, jd_text, payload)

                return {"provider": "groq", "data": result}

            except Exception as e:
                print("❌ Groq ERROR:", str(e))

    # -----------------------------
    # FALLBACK
    # -----------------------------
 
        return {
            "provider": "none",
            "data": {
                "summary": "AI insights temporarily unavailable.",
                "strengths": [],
                "weaknesses": [],
                "opportunities": [],
                "threats": [],
                "role_fit": [],
                "career_advice": "Please try again later."
            }
        }
        