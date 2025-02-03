from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

from api.chatCompletionsRouter import router as api_chat_router
from api.embeddingsRouter import router as api_embedding_router
from api.fineTuningRouter import router as api_finetuning_router
from api.imageRouter import router as api_image_router
from api.moderationsRouter import router as api_moderations_router
from api.speechToTextRouter import router as api_speechtext_router
from api.translateRouter import router as api_translate_router

app = FastAPI()

# Configurações de CORS
def get_cors_origins():
    origins = os.getenv('CORS_ORIGINS')
    if origins:
        return [origin.strip() for origin in origins.split(',')]
    return []

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_cors_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota básica de teste
@app.get("/")
def read_root():
    return {"message": "Server is running!"}


app.include_router(api_chat_router)
app.include_router(api_embedding_router)
app.include_router(api_finetuning_router)
app.include_router(api_image_router)
app.include_router(api_moderations_router)
app.include_router(api_speechtext_router)
app.include_router(api_translate_router)

