
# Chat completions (ex: Mistral-Nemo-Instruct-2407)
from fastapi import APIRouter
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

HUGGING_FACE_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-Nemo-Instruct-2407"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

router = APIRouter()

class ChatRequest(BaseModel):
    prompt: str
    max_length: int = 100

@router.post("/api/chat_completion")
async def chat_completion(request: ChatRequest):
    payload = {
        "inputs": request.prompt,
        "parameters": {"max_length": request.max_length},
    }

    response = requests.post(HUGGING_FACE_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

