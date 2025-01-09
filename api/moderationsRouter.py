# Moderations (Hate-speech-CNERG/dehatebert-mono-english)
from fastapi import APIRouter
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

HUGGING_FACE_API_URL = "https://api-inference.huggingface.co/models/facebook/wav2vec2-large-960h-lv60"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

router = APIRouter()

class ModerationRequest(BaseModel):
    text: str

@router.post("api/moderations")
async def moderate_text(request: ModerationRequest):
    payload = {"inputs": request.text}
    response = requests.post(HUGGING_FACE_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()