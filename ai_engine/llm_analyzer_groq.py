from groq import Groq
import os
import json
import re
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env")



class GroqAnalyzer:

    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def _build_prompt(self, resume_text, jd_text, scores):
        return f"""
You are a highly intelligent career analyst and recruiter.

Your goal is to extract deep, human-like insights —
NOT generic summaries.

Focus on:
- real capability vs claimed skill
- depth of experience
- growth signals
- practical exposure
- job readiness
- "summary" MUST NOT be empty
- "career_advice" MUST be actionable and non-empty

----------------------------------------

Resume:
{resume_text}

Job Description:
{jd_text}

Scores:
{json.dumps(scores)}

----------------------------------------

RULES:

- Think like a recruiter, not a keyword matcher
- Avoid generic advice
- Be specific, insightful, and honest

----------------------------------------

OUTPUT (STRICT JSON ONLY):

{{
  "summary": "",
  "strengths": [],
  "weaknesses": [],
  "opportunities": [],
  "threats": [],
  "role_fit": [
    {{
      "role": "",
      "fit_score": 0,
      "reason": ""
    }}
  ],
  "career_advice": ""
}}
"""

    def generate_insights(self, resume_text, jd_text, scores):

        prompt = self._build_prompt(resume_text, jd_text, scores)

        try:
            response = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": "Return ONLY valid JSON."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )

            content = response.choices[0].message.content.strip()

            cleaned = re.sub(r"```json|```", "", content).strip()

            return json.loads(cleaned)

        except json.JSONDecodeError:
            return {
                "error": "JSON parsing failed",
                "raw_output": content
            }

        except Exception as e:
            raise Exception(f"Groq Error: {str(e)}")
    
    def generate_custom(self, prompt):
        response = self.client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Return ONLY valid JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

        content = response.choices[0].message.content.strip()

        cleaned = re.sub(r"```json|```", "", content).strip()

        return json.loads(cleaned)