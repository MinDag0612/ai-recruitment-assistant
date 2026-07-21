from app.features.resume.repository import ResumeRepository
from app.features.resume.parser import ParserCV
from app.models.resume import Resume

from fastapi import UploadFile


class ResumeService:
    def __init__(self, repository: ResumeRepository, parser: ParserCV):
        self.repository = repository
        self.parser = parser
    
    def store_resume(self, file: UploadFile, cv_name: str) -> Resume:
        parsed_text = self.parser.parse(file = file)
        
        resume = Resume(
            cv_name=cv_name,
            file_name=file.filename,
            file_url = "...",
            parsed_text=parsed_text
        )
        
        resume = self.repository.create(resume=resume)
        
        return resume