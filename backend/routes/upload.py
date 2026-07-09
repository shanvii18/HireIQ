from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from ai_engine.parser import extract_text
from backend.services.analyzer_service import get_full_analysis

router = APIRouter(tags=["Upload"])


@router.post("/upload-analyze")
async def upload_analyze(
    file: UploadFile = File(...),
    jd_text: str = Form(...)
):
    try:
        file_bytes = await file.read()
        resume_text = extract_text(file_bytes)

        # ✅ FIX: yahan change
        result = get_full_analysis(resume_text, jd_text)

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Upload analysis failed: {str(e)}"
        )