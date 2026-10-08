from app.core.database import get_session
from fastapi import APIRouter, Depends
from sqlmodel import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.features.auth.schema import RegisterInfor, LoginInfor
from app.features.auth.service import UserService
from app.features.auth.repository import UserRepo

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
    return service.register_user(infor=user_infor)

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):
    login_infor = LoginInfor(
        email=form_data.username,
        password=form_data.password
    )
    service = UserService(
        repo=UserRepo(
            session=session
        )
    )
    
    return service.login(
        login_infor=login_infor
    )