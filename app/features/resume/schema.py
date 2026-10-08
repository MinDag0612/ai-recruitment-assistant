from app.enum.resumeStatus import ResumeStatus
from uuid import UUID, uuid4

from pydantic import BaseModel

class ResumeUploadResponse(BaseModel):
    id: UUID
    cv_name: str
    file_name: str
    status: ResumeStatus