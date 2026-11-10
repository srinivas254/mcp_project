from fastapi import APIRouter
from app.models.request_model import (
    ChatRequest
)
from app.models.response_model import (
    ChatResponse
)

from app.services.llm_service import (
    llm_call
)

router = APIRouter()

@router.get("/status")
async def health_check():
    return "healthy!!"

@router.post("/chat", response_model=ChatResponse)
async def retrieve_solution(request: ChatRequest):
    response = llm_call(request.query)

    return ChatResponse(
        query=request.query,
        response=response
    )


