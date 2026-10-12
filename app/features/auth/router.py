from app.core.database import get_session
from fastapi import APIRouter, Depends
from sqlmodel import Session
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import ValidationError

from app.features.auth.schema import RegisterInfor, LoginInfor
from app.features.auth.service import UserService
from app.features.auth.repository import UserRepo
from app.core.response.exception_type import InvalidCredentialsError


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(
    user_infor: RegisterInfor,
    session: Session = Depends(get_session)
):
    service = UserService(
        repo=UserRepo(
            session=session
        )
    )
    return service.register_user(register_infor=user_infor)

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):
    try:
        login_infor = LoginInfor(
            email=form_data.username,
            password=form_data.password
        )
    except ValidationError as exc:
        messages = [
            error["msg"]
            for error in exc.errors()
        ]

        raise InvalidCredentialsError(
            "; ".join(messages)
        ) from exc
        
    service = UserService(
        repo=UserRepo(
            session=session
        )
    )
    
    return service.login(
        login_infor=login_infor
    )