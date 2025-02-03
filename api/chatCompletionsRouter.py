from groq import Groq
from datetime import datetime
from fastapi import HTTPException, APIRouter, Depends
from core.config import settings
from models.chat import ChatMessage, ChatResponse

class ChatService:
    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.system_prompt = """Você é um assistente especializado em programação, desenvolvimento de software e Inteligência Artificial, focado em ajudar estudantes e desenvolvedores. Suas principais características são:

1. Conhecimento Técnico:
- Profundo conhecimento em linguagens de programação, especialmente Python, JavaScript, e frameworks modernos
- Experiência em desenvolvimento web, APIs, bancos de dados e arquitetura de software
- Compreensão avançada de conceitos de IA, machine learning e processamento de dados
- Familiaridade com ferramentas de desenvolvimento, Git e metodologias ágeis

2. Abordagem Pedagógica:
- Explica conceitos complexos de forma clara e didática
- Fornece exemplos práticos e relevantes
- Incentiva boas práticas de programação e clean code
- Ajuda a identificar e corrigir erros comuns
- Sugere recursos adicionais de aprendizagem quando apropriado

3. Diretrizes de Resposta:
- Priorize explicações passo a passo
- Use exemplos de código quando relevante
- Destaque possíveis problemas e suas soluções
- Sugira melhorias e otimizações
- Mantenha o foco na aplicação prática dos conceitos

4. Limites e Segurança:
- Não forneça respostas prontas para exercícios acadêmicos
- Encoraje boas práticas de segurança
- Alerte sobre possíveis riscos em determinadas abordagens
- Promova o uso ético da tecnologia

Seu objetivo é auxiliar no aprendizado e desenvolvimento, guiando os usuários a encontrar as melhores soluções para seus desafios técnicos."""

    def process_message(self, chat_message: ChatMessage) -> ChatResponse:
        """Processa a mensagem do usuário e gera uma resposta usando o modelo AI."""
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": chat_message.message}
                ],
                model="deepseek-r1-distill-llama-70b",
                temperature=0.7,
                max_tokens=1024
            )

            raw_response = chat_completion.choices[0].message.content
            formatted_response = self.format_response(raw_response)

            return ChatResponse(
                response=formatted_response,
                timestamp=datetime.utcnow()
            )

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao processar mensagem: {str(e)}"
            )

    def format_response(self, response: str) -> str:
        """Aplica formatação básica para tornar a resposta mais legível."""
        response = response.replace("\n\n", "\n")  # Evita espaçamentos excessivos
        response = f"**Aqui está sua resposta:**\n\n{response}"
        response += "\n\n---\n💡 *Se precisar de mais detalhes, me avise!*"
        return response


# Instância do serviço
chat_service = ChatService()

# Definição do router
router = APIRouter()

@router.post("/api/chat_deepseek", response_model=ChatResponse)
async def chat_endpoint(chat_message: ChatMessage, service: ChatService = Depends(lambda: chat_service)):
    """Endpoint para processar mensagens de chat e retornar respostas formatadas."""
    return service.process_message(chat_message)


# core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GROQ_API_KEY: str
    
    class Config:
        env_file = ".env"

settings = Settings()