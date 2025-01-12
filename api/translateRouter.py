from fastapi import APIRouter
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

HUGGING_FACE_API_URL = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-many-mmt"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

router = APIRouter()

class TranslationRequest(BaseModel):
    text: str
    src_lang: str
    tgt_lang: str

@router.post("/api/translate")
async def translate_text(request: TranslationRequest):
    payload = {
        "inputs": request.text,
        "parameters": {
            "src_lang": request.src_lang,
            "tgt_lang": request.tgt_lang
        }
    }
    response = requests.post(HUGGING_FACE_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()