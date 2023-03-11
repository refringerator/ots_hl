from typing import List
from fastapi import FastAPI

from models import (
    LoginPostRequest,
    LoginPostResponse,
    ErrorResponse,
    User,
    UserRegisterPostRequest,
    UserRegisterPostResponse,
)

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
    pass


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
    pass


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
    pass


