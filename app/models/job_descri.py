from sqlmodel import Field
from uuid import UUID, uuid4

from app.models.base import BaseModel
from app.enum.jobDescripStatus import JobDescripStatus

class JobDescrip(BaseModel, table=True):
    jd_name: str
    file_name: str
    file_url: str
    parsed_text: str
    status: JobDescripStatus = Field(default=JobDescripStatus.PENDING)
    
    user_id: UUID = Field(foreign_key="user.id")