import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi import FastAPI
from backend.routes import analysis, upload

app = FastAPI(title="HireIQ API")

app.include_router(analysis.router)
app.include_router(upload.router)

@app.get("/")
def home():
    return {"message": "HireIQ running"}