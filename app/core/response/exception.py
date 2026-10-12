
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.response.exception_type import InvalidCredentialsError, InvalidFileExtension
from app.core.response.base_response import BaseResponse


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    messages = [
        error["msg"]
        for error in exc.errors()
    ]

    response = BaseResponse(
        error="VALIDATION_ERROR",
        msg="; ".join(messages),
        data=None,
    )

    return JSONResponse(
        status_code=422,
        content=response.model_dump(mode="json"),
    )
    
async def invalid_user_infor_handler(
    request: Request,
    exc: InvalidCredentialsError,
):
    response = BaseResponse(
        error="INVALID USER INFORMATION",
        msg=str(exc),
        data=None,
    )

    return JSONResponse(
        status_code=401,
        content=response.model_dump(mode="json"),
    )


async def invalid_credentials_handler(
    request: Request,
    exc: InvalidCredentialsError,
):
    response = BaseResponse(
        error="INVALID_CREDENTIALS",
        msg=str(exc),
        data=None,
    )

    return JSONResponse(
        status_code=401,
        content=response.model_dump(mode="json"),
    )

async def invalid_file_extension_handler(
    request: Request,
    exc: InvalidFileExtension,
):
    response = BaseResponse(
        error="UNSUPPORTED FILE TYPE",
        msg=str(exc),
        data=None,
    )

    return JSONResponse(
        status_code=400,
        content=response.model_dump(mode="json"),
    )
    
async def invalid_file_extension_handler(
    request: Request,
    exc: InvalidFileExtension,
):
    response = BaseResponse(
        error="UNSUPPORTED FILE TYPE",
        msg=str(exc),
        data=None,
    )

    return JSONResponse(
        status_code=400,
        content=response.model_dump(mode="json"),
    )