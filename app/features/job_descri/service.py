from app.features.job_descri.parser import FakeParserJD
from app.models.job_descri import JobDescrip
from app.features.job_descri.repository import JdRepo

from fastapi import UploadFile

class JobDescriptService:
    def __init__(self, repo: JdRepo, parser: FakeParserJD):
        self.parser = parser
        self.repo = repo
        
    def store_jd(self, file: UploadFile, jd_name: str):
        parsed_text = self.parser.parse(file=file)
        
        jd = JobDescrip(
            jd_name=jd_name,
            file_name=file.filename,
            file_url = "...",
            parsed_text=parsed_text
        )
        
        jd = self.repo.create(jd=jd)
        
        print(type(jd))
        print(jd.model_dump())
        print(jd.__table__)
        
        return jd