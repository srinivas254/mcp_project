from pydantic import BaseModel

class ChatResponse(BaseModel):
    query: str
    response: str