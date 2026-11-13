from fastapi.responses import JSONResponse, Request
from app.Exceptions.myExceptions import (
    ToolExecutionError
)

async def tool_execution_exception_handler(
    request: Request,
    exc: ToolExecutionError
) -> JSONResponse:

    return JSONResponse(
        content={
            "message": str(exc)
        },
        status_code=500
    )
