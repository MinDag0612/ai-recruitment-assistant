from sqlmodel import Field
from pydantic import EmailStr


from app.models.base import BaseModel
from app.enum.jobDescripStatus import JobDescripStatus

class User(BaseModel, table=True):
    username: str
    email: EmailStr = Field(unique=True, index=True)
    password_hash: str