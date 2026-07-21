from sqlmodel import Session
from uuid import UUID, uuid4

from app.models.resume import Resume

class ResumeRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, resume: Resume) -> Resume:
        self.session.add(resume)
        self.session.commit()
        self.session.refresh(resume)
        
        return resume

    def get_by_id(self, resume_id: UUID) -> Resume | None:
        ...

    def update(self, resume: Resume) -> Resume:
        ...
    