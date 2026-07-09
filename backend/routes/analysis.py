from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
import logging

from backend.services.analyzer_service import get_full_analysis

# Logger setup
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/analyze",
    tags=["Analysis"]
)


# -----------------------------
# Request Schema
# -----------------------------
class AnalyzeRequest(BaseModel):
    resume_text: str = Field(..., min_length=10)
    jd_text: str = Field(..., min_length=10)


# -----------------------------
# Response Schema (important for production)
# -----------------------------
class AnalyzeResponse(BaseModel):
    ats_score: float
    cosine_score: float
    skill_match_percent: float
    matched_skills: list[str]
    missing_skills: list[str]
    insights: dict
    llm_used: str
    questions: dict


# -----------------------------
# Endpoint
# -----------------------------
@router.post("/", response_model=AnalyzeResponse, status_code=status.HTTP_200_OK)
def analyze(data: AnalyzeRequest):
    try:
        logger.info("Analysis request received")

        result = get_full_analysis(
            data.resume_text,
            data.jd_text
        )

        logger.info("Analysis completed successfully")

        return result

    except ValueError as ve:
        logger.warning(f"Validation/Value error: {str(ve)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ve)
        )

    except Exception as e:
        logger.error(f"Internal error: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error. Please try again later."
        )