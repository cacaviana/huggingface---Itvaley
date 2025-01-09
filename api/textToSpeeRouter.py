# textToSpee (parler-tts/parler-tts-large-v1)
from fastapi import APIRouter
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

HUGGING_FACE_API_URL = "https://api-inference.huggingface.co/models/parler-tts/parler-tts-large-v1"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

router = APIRouter()

class TTSRequest(BaseModel):
    text: str

@router.post("/api/tts")
async def text_to_text(request: TTSRequest):
    payload = {"inputs": request.text}
    response = requests.post(HUGGING_FACE_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()