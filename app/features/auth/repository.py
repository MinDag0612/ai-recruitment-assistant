from sqlmodel import Session
from uuid import UUID, uuid4
from sqlmodel import select

from app.models.user import User

class UserRepo:
    def __init__(self, session: Session):
        self.session = session
        
    def create(self, user: User):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        
        return user
    
    def get_by_email(self, email: str):
        statement = select(User).where(User.email == email)
        user = self.session.exec(statement).first()

        return user