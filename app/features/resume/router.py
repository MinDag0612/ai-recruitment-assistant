from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlmodel import Session
from typing import Annotated

from app.core.database import get_session
from app.features.resume.parser import FakeParserCV
from app.features.resume.repository import ResumeRepository
from app.features.resume.service import ResumeService
from app.features.validation.validate_file import ValidateFile
from app.features.storage.LocalStorage import LocalStorage

router = APIRouter(prefix="/Resume", tags=["Resume"])


@router.post("/upload")
def upload_resume(
    file: Annotated[UploadFile, Depends(ValidateFile.validate_upload_file)], 
    cv_name: str = Form(...), 
    session: Session = Depends(get_session)
):
    service = ResumeService(
        repository=ResumeRepository(session),
        parser=FakeParserCV(),
        storage=LocalStorage("resume"),
    )

    return service.store_resume(file, cv_name)