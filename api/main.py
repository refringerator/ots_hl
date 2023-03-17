from fastapi import FastAPI

from models import (
    LoginPostRequest,
    LoginPostResponse,
    ErrorResponse,
    User,
    UserRegisterPostRequest,
    UserRegisterPostResponse,
)
from auth import Auth
from fastapi import FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from users import get_user_by_id, authenticate_user, register_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
auth_handler = Auth()


app = FastAPI(
    title="OTUS Highload Architect",
    version="1.0.0",
)


@app.post(
    "/login",
    response_model=LoginPostResponse,
    responses={
        "500": {"model": ErrorResponse},
        "503": {"model": ErrorResponse},
    },
)
def post_login(
    body: LoginPostRequest = None,
) -> LoginPostResponse | ErrorResponse:
    user = authenticate_user(body.id, body.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    token = auth_handler.create_access_token(data={"sub": body.id})
    return LoginPostResponse(token=token)


@app.get(
    "/user/get/{id}",
    response_model=User,
    responses={
        "500": {"model": ErrorResponse},
        "503": {"model": ErrorResponse},
    },
)
def get_user_get_id(
    id: str,
) -> User | ErrorResponse:
    user_data = get_user_by_id(id)[0]
    return User(**user_data)


@app.post(
    "/user/register",
    response_model=UserRegisterPostResponse,
    responses={
        "500": {"model": ErrorResponse},
        "503": {"model": ErrorResponse},
    },
)
def post_user_register(
    body: UserRegisterPostRequest = None,
) -> UserRegisterPostResponse | ErrorResponse:
    user_id = register_user(body)
    return UserRegisterPostResponse(user_id=user_id)
