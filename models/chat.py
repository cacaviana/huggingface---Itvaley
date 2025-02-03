from pydantic import BaseModel
from datetime import datetime

class ChatMessage(BaseModel):
    message: str
    user_id: str = "default_user"  # Opcional, caso você queira manter identificação

class ChatResponse(BaseModel):
    response: str
    timestamp: datetime