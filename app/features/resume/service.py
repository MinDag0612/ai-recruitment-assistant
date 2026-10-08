from app.features.resume.repository import ResumeRepository
from app.features.resume.parser import ParserCV
from app.models.resume import Resume
from app.features.resume.schema import ResumeUploadResponse
from app.features.storage.Storage import Storage
from app.dependencies.auth import get_current_user_id

from fastapi import UploadFile
from uuid import UUID

class ResumeService:
    def __init__(
        self,
        repository: ResumeRepository,
        parser: ParserCV,
        storage: Storage,
        user_id: UUID
    ):
        self.repository = repository
        self.parser = parser
        self.storage = storage
        self.user_id = user_id
    
    def store_resume(self, file: UploadFile, cv_name: str) -> Resume:
        parsed_text = self.parser.parse(file = file)
        file_url = self.storage.store(file=file)
        
        resume = Resume(
            cv_name=cv_name,
            file_name=file.filename,
            file_url=file_url,
            parsed_text=parsed_text,
            user_id=self.user_id
        )
        
        resume = self.repository.create(resume=resume)
        
        return ResumeUploadResponse(
            id=resume.id,
            cv_name=resume.cv_name,
            file_name=resume.file_name,
            status=resume.status
        )