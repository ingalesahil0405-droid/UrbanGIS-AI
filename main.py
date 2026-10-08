import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from anthropic import Anthropic

load_dotenv()

app = FastAPI(title="UrbanGIS AI", version="0.1.0")
STATIC_DIR = Path(__file__).resolve().parent.parent / "static"


class AnalysisRequest(BaseModel):
    question: str
    context: str = ""


@app.get("/")
def home():
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/api/analyze")
def analyze(request: AnalysisRequest):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return {
            "ok": False,
            "error": "ANTHROPIC_API_KEY is not configured. Copy .env.example to .env and add your key."
        }

    client = Anthropic(api_key=api_key)
    model = os.getenv("ANTHROPIC_MODEL", "claude-opus-5-5")

    prompt = f"""
You are UrbanGIS AI, an assistant for urban planners and GIS professionals.

User question:
{request.question}

GIS/project context:
{request.context or "No additional context supplied."}

Provide:
1. A concise interpretation.
2. Relevant GIS/planning factors to examine.
3. A practical next-step workflow.
4. Important limitations or validation checks.

Do not invent measurements, statistics, laws, or map results that were not supplied.
"""

    try:
        message = client.messages.create(
            model=model,
            max_tokens=1200,
            messages=[{"role": "user", "content": prompt}],
        )
        text = "\n".join(
            block.text for block in message.content
            if getattr(block, "type", None) == "text"
        )
        return {"ok": True, "answer": text}
    except Exception as exc:
        return {"ok": False, "error": str(exc)}
