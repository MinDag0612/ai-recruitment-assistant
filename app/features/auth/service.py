from app.features.auth.repository import UserRepo
from app.features.auth.schema import RegisterInfor, RegisterReturn, LoginInfor, LoginReturn
from app.models.user import User
from app.features.auth.hasher import Hasher
from app.core.jwt import JWTHandler
from app.core.exception_type import InvalidCredentialsError

from fastapi import UploadFile

class UserService:
    def __init__(self, repo: UserRepo):
        self.repo = repo
        
    def register_user(self, register_infor: RegisterInfor):
        password_hash = Hasher.hash(register_infor.password)
        
        user = User(
            username=register_infor.username,
            email=register_infor.email,
            password_hash=password_hash
        )
        
        user = self.repo.create(user=user)
        
        return RegisterReturn(
            id=user.id,
            username=user.username,
            email=user.email
        )
        
    def login(self, login_infor: LoginInfor):
        user = self.repo.get_by_email(
            email=login_infor.email
        )

        if not user:
            raise InvalidCredentialsError(
                "Invalid email or password"
            )

        if not Hasher.verify(
            password=login_infor.password,
            hashed_password=user.password_hash,
        ):
            raise InvalidCredentialsError(
                "Invalid email or password"
            )

        access_token = JWTHandler.encode(
            user_id=user.id
        )

        return LoginReturn(
            access_token=access_token
        )