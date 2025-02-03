# # # textToSpee (parler-tts/parler-tts-large-v1)
# # from fastapi import APIRouter
# # from pydantic import BaseModel
# # import os
# # import requests
# # from dotenv import load_dotenv

# # # Carregar variáveis de ambiente
# # load_dotenv()
# # API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

# # HUGGING_FACE_API_URL = "https://api-inference.huggingface.co/models/parler-tts/parler-tts-large-v1"
# # headers = {"Authorization": f"Bearer {API_TOKEN}"}

# # router = APIRouter()

# # class TTSRequest(BaseModel):
# #     text: str

# # @router.post("/api/tts")
# # async def text_to_text(request: TTSRequest):
# #     payload = {"inputs": request.text}
# #     response = requests.post(HUGGING_FACE_API_URL, headers=headers, json=payload)
# #     response.raise_for_status()
# #     return response.json()


# # textToSpeech (parler-tts/parler-tts-large-v1)
# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# import os
# import requests
# from dotenv import load_dotenv

# # Carregar variáveis de ambiente
# load_dotenv()
# API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

# # Verificar se a chave da API foi carregada
# if not API_TOKEN:
#     raise ValueError("HUGGINGFACE_API_KEY não foi configurada no arquivo .env.")

# HUGGING_FACE_API_URL = "https://api-inference.huggingface.co/models/parler-tts/parler-tts-large-v1"
# headers = {"Authorization": f"Bearer {API_TOKEN}"}

# router = APIRouter()

# class TTSRequest(BaseModel):
#     text: str

# @router.post("/api/tts")
# async def text_to_speech(request: TTSRequest):
#     payload = {"inputs": request.text}
    
#     try:
#         response = requests.post(HUGGING_FACE_API_URL, headers=headers, json=payload)
#         response.raise_for_status()
#     except requests.exceptions.RequestException as e:
#         raise HTTPException(status_code=500, detail=f"Erro na chamada para Hugging Face API: {str(e)}")
    
#     # Verificar o tipo de resposta
#     if response.headers.get("content-type") == "audio/mpeg":
#         # Retorna áudio como um arquivo
#         return {
#             "audio_content": response.content
#         }
#     else:
#         # Caso a resposta não seja áudio, retorna o JSON da API
#         return response.json()