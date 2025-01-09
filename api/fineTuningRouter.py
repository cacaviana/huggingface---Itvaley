import requests
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Carregando variáveis de ambiente do .env
load_dotenv()
API_TOKEN = os.getenv("HUGGING_FACE_API_TOKEN")
HUGGING_FACE_API_URL = "https://api-inference.huggingface.co/train"  # Ajuste conforme necessário
headers = {"Authorization": f"Bearer {API_TOKEN}"}

router = APIRouter()

class FineTuningRequest(BaseModel):
    model_id: str  # Modelo base para fine-tuning
    dataset_url: str  # URL pública do dataset para treinamento
    output_model_name: str  # Nome do modelo ajustado
    parameters: dict = {}  # Parâmetros opcionais para fine-tuning

@router.post("/api/fine_tuning")
async def fine_tune_model(request: FineTuningRequest):
    """
    Endpoint para realizar fine-tuning em um modelo.
    """
    payload = {
        "model_id": request.model_id,
        "dataset": {"url": request.dataset_url},
        "output_model_name": request.output_model_name,
        "parameters": request.parameters,
    }

    try:
        response = requests.post(HUGGING_FACE_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro no fine-tuning: {str(e)}")