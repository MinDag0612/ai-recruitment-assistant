from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.core.exception_type import InvalidCredentialsError


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    errors = exc.errors()

    messages = [
        error["msg"]
        for error in errors
    ]

    return JSONResponse(
        status_code=422,
        content={
            "error": "VALIDATION_ERROR",
            "msg": messages,
        },
    )
    
async def invalid_credentials_handler(
    request: Request,
    exc: InvalidCredentialsError,
):
    return JSONResponse(
        status_code=401,
        content={
            "error": "INVALID_CREDENTIALS",
            "msg": str(exc),
        },
    )