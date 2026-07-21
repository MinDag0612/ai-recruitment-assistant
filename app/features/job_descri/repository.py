from sqlmodel import Session
from uuid import UUID, uuid4

from app.models.job_descri import JobDescrip

class JdRepo:
    def __init__(self, session: Session):
        self.session = session
        
    def create(self, jd: JobDescrip):
        self.session.add(jd)
        self.session.commit()
        self.session.refresh(jd)
        
        return jd
        