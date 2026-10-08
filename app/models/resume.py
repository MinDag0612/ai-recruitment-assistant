from sqlmodel import Field
from uuid import UUID, uuid4

from app.models.base import BaseModel
from app.enum.resumeStatus import ResumeStatus

class Resume(BaseModel, table=True):
    cv_name: str
    file_name: str
    file_url: str
    parsed_text: str
    status: ResumeStatus = Field(default=ResumeStatus.PENDING)
    
    user_id: UUID = Field(foreign_key="user.id")