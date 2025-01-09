from fastapi import FastAPI

from api.chatCompletionsRouter import router as api_chat_router
from api.embeddingsRouter import router as api_embedding_router
from api.fineTuningRouter import router as api_finetuning_router
from api.imageRouter import router as api_image_router
from api.moderationsRouter import router as api_moderations_router
from api.speechToTextRouter import router as api_speechtext_router
from api.textToSpeeRouter import router as api_texttospeech_router
from api.translateRouter import router as api_translate_router

app = FastAPI()

app.include_router(api_chat_router)
app.include_router(api_embedding_router)
app.include_router(api_finetuning_router)
app.include_router(api_image_router)
app.include_router(api_moderations_router)
app.include_router(api_speechtext_router)
app.include_router(api_texttospeech_router)
app.include_router(api_translate_router)

