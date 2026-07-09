# 🚀 HireIQ – AI Powered Campus Placement Intelligence System

HireIQ is an AI-driven platform designed to evaluate real placement readiness of students by analyzing resumes against job descriptions and generating intelligent insights.

Unlike traditional ATS tools, HireIQ focuses on depth of skills, practical exposure, and interview readiness — not just keyword matching.

Current Stage: Core Resume Intelligence Engine (MVP)

---

## Core Features

- ATS Score Calculation  
- Resume vs JD Matching (Cosine Similarity)  
- AI-Powered Insights (LLM-based analysis)  
- Skill Gap Detection  
- Interview Question Generator (based on gaps)  
- FastAPI-based backend  

---

## What Makes It Different?

- Goes beyond keyword matching → analyzes real capability vs claimed skills  
- Identifies depth gaps in experience  
- Generates role-specific interview questions  
- Designed as a foundation for a full placement ecosystem  

---

## Tech Stack

- Backend: FastAPI (Python)  
- AI/NLP: TF-IDF, Cosine Similarity  
- LLM: Groq / OpenAI  
- Architecture: Modular AI Engine  
- Other: Uvicorn, Pydantic  

---

## Project Structure

HireIQ/
  ai_engine/        (Core ML + LLM logic)
  backend/          (FastAPI APIs)
  frontend/         (In Progress)
  requirements.txt
  .gitignore

---

## Setup Instructions

git clone https://github.com/shanvii18/HireIQ.git  
cd HireIQ  

pip install -r requirements.txt  

Create a .env file:

GROQ_API_KEY=your_key  
OPENAI_API_KEY=your_key  

Run server:

uvicorn backend.main:app --reload  

---

## API Endpoint

POST /analyze/

Request:

{
  "resume_text": "...",
  "jd_text": "..."
}

Response includes:

- ATS Score  
- Skill Match %  
- Missing Skills  
- AI Insights  
- Interview Questions  

---

## Vision (Big Picture)

HireIQ is being built as a complete campus placement intelligence system:

- Student Dashboard (resume + skill tracking)  
- Recruiter Panel (candidate ranking)  
- Placement Analytics (college-level insights)  
- AI Interview Preparation System  

Current module acts as the core intelligence engine powering this ecosystem.

---

## Future Improvements

- Frontend UI  
- Resume Upload (PDF parsing)  
- Multi-JD comparison  
- Candidate ranking system  
- Authentication system  
- Deployment (Docker + Cloud)  

---

## Why This Project?

Most students don’t know their real placement readiness.

HireIQ aims to bridge that gap by providing:

- honest evaluation  
- actionable insights  
- structured preparation guidance  

---

## Author

Shanvi Verma  
B.Tech CSE | Building AI-powered systems
