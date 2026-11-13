from fastapi import FastAPI 
from app.routers.primary import router as primary_router
from app.Exceptions.myExceptions import (
    ToolExecutionError
)
from app.Exceptions.exceptionHandler import (
    tool_execution_exception_handler
)

app = FastAPI()
app.include_router(primary_router)

app.add_exception_handler(
    ToolExecutionError,
    tool_execution_exception_handler
)