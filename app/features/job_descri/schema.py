from uuid import UUID, uuid4
from pydantic import BaseModel

from app.enum.jobDescripStatus import JobDescripStatus

class JobDescripUploadResponse(BaseModel):
    id: UUID
    jd_name: str
    file_name: str
    status: JobDescripStatus