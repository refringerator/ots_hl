from __future__ import annotations

from typing import List, Union

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
) -> Union[User, UserGetIdGetResponse, ErrorResponse]:
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
) -> Union[UserRegisterPostResponse, ErrorResponse]:
    pass


@app.get(
    "/user/search",
    response_model=List[User],
    responses={
        "500": {"model": ErrorResponse},
        "503": {"model": ErrorResponse},
    },
)
def get_user_search(
    first_name: str, last_name: str = ...
) -> Union[List[User], ErrorResponse]:
    pass
