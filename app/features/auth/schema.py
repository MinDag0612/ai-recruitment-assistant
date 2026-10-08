from uuid import UUID, uuid4
from pydantic import BaseModel, Field, EmailStr

class RegisterInfor(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=6)
    
class RegisterReturn(BaseModel):
    id: UUID
    username: str
    email: str
    
class LoginInfor(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
    
class LoginReturn(BaseModel):
    access_token: str
    token_type: str = "bearer"

    