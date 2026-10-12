from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.features.resume.router import router as resume_router
from app.features.job_descri.router import router as job_descrip_router
from app.features.auth.router import router as auth_router
from app.core.response.exception import validation_exception_handler, invalid_credentials_handler, invalid_file_extension_handler, invalid_user_infor_handler
from app.core.response.exception_type import InvalidCredentialsError, InvalidFileExtension, InvalidUserInforError

app = FastAPI()

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler,
)

app.add_exception_handler(
    InvalidCredentialsError,
    invalid_credentials_handler
)

app.add_exception_handler(
    InvalidFileExtension,
    invalid_file_extension_handler
)

app.add_exception_handler(
    InvalidUserInforError,
    invalid_user_infor_handler
)

app.include_router(resume_router)
app.include_router(job_descrip_router)
app.include_router(auth_router)

@app.get("/health")
def check_health():
    return {"message": "API running !!"}