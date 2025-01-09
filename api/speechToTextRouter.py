# Spee to text (wav2vec2-large-960h-lv60)
from fastapi import APIRouter, File, UploadFile
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

@router.post("api/stt")
async def speech_to_text(file: UploadFile = File(...)):
    audio_content = await file.read()
    response = requests.post(HUGGING_FACE_API_URL, headers=headers, data=audio_content)
    response.raise_for_status()
    return response.json()