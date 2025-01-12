# Spee to text (Qwen/Qwen2-Audio-7B)
from fastapi import APIRouter, File, UploadFile, HTTPException
import os
import requests
from dotenv import load_dotenv
from io import BytesIO

# Carregar variáveis de ambiente
load_dotenv()
API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

# URL da API do Hugging Face para o modelo Qwen2-Audio-7B
HUGGING_FACE_API_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2-Audio-7B"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

router = APIRouter()

@router.post("/api/stt")
async def speech_to_text(file: UploadFile = File(...)):
    try:
        # Ler o conteúdo do arquivo de áudio
        audio_content = await file.read()

        # Enviar o áudio para a API do Hugging Face
        response = requests.post(
            HUGGING_FACE_API_URL,
            headers=headers,
            files={"file": ("audio.mp3", BytesIO(audio_content), "audio/mp3")}
        )

        # Verificar se a resposta foi bem-sucedida
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Erro ao processar o áudio na API.")

        # Retornar a resposta da API
        return response.json()

    except requests.exceptions.RequestException as e:
        # Tratar erros de requisição
        raise HTTPException(status_code=500, detail=f"Erro ao processar o áudio na API: {str(e)}")

    except Exception as e:
        # Tratar outros erros
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {str(e)}")