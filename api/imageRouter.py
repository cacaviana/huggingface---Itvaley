# Gerar imagem com (stabilityai/stable-diffusion-3-medium-diffusers)
# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# import os
# import requests
# from dotenv import load_dotenv

# # Carregar variáveis de ambiente
# load_dotenv()
# API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

# HUGGING_FACE_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
# headers = {"Authorization": f"Bearer {API_TOKEN}"}

# router = APIRouter()

# class ImageRequest(BaseModel):
#     prompt: str

# @router.post("/api/image")
# async def generate_image(request: ImageRequest):
#     payload = {"inputs": request.prompt}
#     try:
#         response = requests.post(HUGGING_FACE_API_URL, headers=headers, json=payload)
#         response.raise_for_status()
#         # Verificar se a API retornou um erro ou conteúdo binário
#         if response.headers.get("Content-Type", "").startswith("image/"):
#             return {"message": "Image generated successfully", "image_data": response.content.hex()}
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         raise HTTPException(status_code=503, detail=f"Error connecting to Hugging Face API: {e}")
    
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import requests
import base64
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

HUGGING_FACE_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

router = APIRouter()

class ImageRequest(BaseModel):
    prompt: str

@router.post("/api/image")
async def generate_image(request: ImageRequest):
    payload = {"inputs": request.prompt}
    try:
        response = requests.post(HUGGING_FACE_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            base64_image = base64.b64encode(response.content).decode('utf-8')
            return {"message": "Image generated successfully", "image_data": f"data:image/png;base64,{base64_image}"}
        
        # Handle non-image response (error or other data)
        return response.json()

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail=f"Error connecting to Hugging Face API: {e}")
