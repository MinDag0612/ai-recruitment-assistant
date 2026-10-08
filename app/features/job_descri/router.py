from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlmodel import Session
from app.features.job_descri.service import JobDescriptService
from app.features.job_descri.repository import JdRepo
from app.features.job_descri.parser import FakeParserJD
from app.features.validation.validate_file import ValidateFile
from app.features.storage.LocalStorage import LocalStorage
from app.dependencies.auth import get_current_user_id

from uuid import UUID
from typing import Annotated
from app.core.database import get_session

router = APIRouter(
    prefix="/jobDescrip", 
    tags=["jobDescrip"],
    dependencies=[Depends(get_current_user_id)]
)

@router.post("/upload")
def upload_job_descrip(
    file: Annotated[UploadFile, Depends(ValidateFile.validate_upload_file)], 
    user_id: UUID = Depends(get_current_user_id),
    jd_name: str = Form(...), 
    session: Session = Depends(get_session)
    ):
    
    service = JobDescriptService(
        repo=JdRepo(session=session), 
        parser=FakeParserJD(),
        storage=LocalStorage("jd")
    )
    
    return service.store_jd(file=file, jd_name=jd_name)