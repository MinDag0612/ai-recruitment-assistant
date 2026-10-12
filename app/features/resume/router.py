from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlmodel import Session
from typing import Annotated
from uuid import UUID

from app.core.database import get_session
from app.features.resume.repository import ResumeRepository
from app.features.resume.service import ResumeService
from app.features.validation.validate_file import ValidateFile
from app.features.storage.LocalStorage import LocalStorage
from app.dependencies.auth import get_current_user_id
from app.features.parser.parser_factory import ParserFactory

router = APIRouter(
    prefix="/Resume", 
    tags=["Resume"], 
    dependencies=[Depends(get_current_user_id)]
)


@router.post("/upload")
def upload_resume(
    file: Annotated[UploadFile, Depends(ValidateFile.validate_upload_file)], 
    cv_name: str = Form(...), 
    user_id: UUID = Depends(get_current_user_id),
    session: Session = Depends(get_session)
):
    service = ResumeService(
        user_id=user_id,
        repository=ResumeRepository(session),
        parser=ParserFactory.get_factory(file=file),
        storage=LocalStorage("resume"),
    )

    return service.store_resume(file, cv_name)