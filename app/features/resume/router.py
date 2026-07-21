from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlmodel import Session

from app.core.database import get_session
from app.features.resume.parser import FakeParserCV
from app.features.resume.repository import ResumeRepository
from app.features.resume.service import ResumeService

router = APIRouter(prefix="/Resume", tags=["Resume"])


@router.post("/upload")
def upload_resume(file: UploadFile = File(...), cv_name: str = Form(...), session: Session = Depends(get_session)):
    service = ResumeService(
        repository=ResumeRepository(session),
        parser=FakeParserCV(),
    )

    return service.store_resume(file, cv_name)