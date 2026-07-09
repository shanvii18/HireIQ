from openai import OpenAI
import os
import json
import re
from dotenv import load_dotenv

# Load environment variables
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))
# Get API key
api_key = os.getenv("OPENAI_API_KEY")


# Initialize OpenAI client
client = OpenAI(api_key=api_key)


class OpenAIAnalyzer:

    def generate_insights(self, resume_text, jd_text, scores):

        prompt = f"""
You are a world-class career strategist, recruiter, and mentor combined.

Your job is NOT to simply analyze a resume —
Your job is to deeply understand the PERSON behind the resume.

Think beyond keywords and scores.
Identify intent, effort, learning curve, and hidden strengths.

Bridge the gap between:
- AI-generated scores
- and the real human potential reflected in the resume

Be insightful, slightly critical where needed, but constructive and motivating.

Avoid generic statements. Every insight must feel personal and specific.

--------------------------------------------------

CONTEXT:

Resume:
{resume_text}

Job Description:
{jd_text}

System Scores:
{json.dumps(scores)}

--------------------------------------------------

INSTRUCTIONS:

1. Interpret the resume like a recruiter who actually cares about potential.
2. Do NOT just repeat resume content.
3. Highlight:
   - Depth vs superficial knowledge
   - Real strengths vs claimed skills
   - Missing exposure vs missing skills
4. Identify patterns:
   - Is the candidate a builder, learner, or follower?
   - Is their experience practical or theoretical?
5. Suggest realistic and strategic career direction.

--------------------------------------------------

OUTPUT RULES (VERY IMPORTANT):

- Return ONLY valid JSON
- No markdown, no explanations outside JSON

--------------------------------------------------

OUTPUT FORMAT:

{{
  "summary": "A sharp, human-like summary of the candidate’s profile and potential",

  "strengths": [
    "Real strengths backed by evidence or inference"
  ],

  "weaknesses": [
    "Actual gaps (not generic), including depth issues or missing exposure"
  ],

  "opportunities": [
    "Where the candidate can realistically grow or pivot"
  ],

  "threats": [
    "Market risks, competition gaps, or profile weaknesses"
  ],

  "role_fit": [
    {{
      "role": "Most suitable role",
      "fit_score": 0,
      "reason": "Clear reasoning why this role fits"
    }}
  ],

  "career_advice": "Actionable, practical, and honest next steps for the candidate"
}}
"""

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You must return ONLY valid JSON. Do not include ```json or any extra text."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4
            )

            content = response.choices[0].message.content.strip()

            # Clean markdown if model adds it
            cleaned = re.sub(r"```json|```", "", content).strip()

            return json.loads(cleaned)

        except json.JSONDecodeError:
            return {
                "error": "JSON parsing failed",
                "raw_output": content
            }

        except Exception as e:
            return {
                "error": str(e)
            }
    def generate_custom(self, prompt):

      response = self.client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Return ONLY valid JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

      return json.loads(response.choices[0].message.content)