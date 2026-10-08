from app.features.job_descri.parser import FakeParserJD
from app.models.job_descri import JobDescrip
from app.features.job_descri.repository import JdRepo
from app.features.job_descri.schema import JobDescripUploadResponse
from app.features.storage.Storage import Storage

from fastapi import UploadFile

class JobDescriptService:
    def __init__(self, repo: JdRepo, parser: FakeParserJD, storage: Storage):
        self.parser = parser
        self.repo = repo
        self.storage = storage
        
    def store_jd(self, file: UploadFile, jd_name: str):
        parsed_text = self.parser.parse(file=file)
        file_url = self.storage.store(file=file)
        
        jd = JobDescrip(
            jd_name=jd_name,
            file_name=file.filename,
            file_url = file_url,
            parsed_text=parsed_text
        )
        
        jd = self.repo.create(jd=jd)
        
        return JobDescripUploadResponse(
            id=jd.id,
            jd_name=jd.jd_name,
            file_name=jd.file_name,
            status=jd.status
        )