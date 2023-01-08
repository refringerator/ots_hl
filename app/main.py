# generated by fastapi-codegen:
#   filename:  openapi.json
#   timestamp: 2023-01-08T21:56:42+00:00

from __future__ import annotations

from typing import List, Union

from fastapi import FastAPI

from .models import (
    LoginPostRequest,
    LoginPostResponse,
    LoginPostResponse1,
    LoginPostResponse2,
    User,
    UserGetIdGetResponse,
    UserGetIdGetResponse1,
    UserRegisterPostRequest,
    UserRegisterPostResponse,
    UserRegisterPostResponse1,
    UserRegisterPostResponse2,
    UserSearchGetResponse,
    UserSearchGetResponse1,
)

app = FastAPI(
    title="OTUS Highload Architect",
    version="1.0.0",
)


@app.post(
    "/login",
    response_model=LoginPostResponse,
    responses={
        "500": {"model": LoginPostResponse1},
        "503": {"model": LoginPostResponse2},
    },
)
def post_login(
    body: LoginPostRequest = None,
) -> Union[LoginPostResponse, LoginPostResponse1, LoginPostResponse2]:
    pass


@app.get(
    "/user/get/{id}",
    response_model=User,
    responses={
        "500": {"model": UserGetIdGetResponse},
        "503": {"model": UserGetIdGetResponse1},
    },
)
def get_user_get_id(
    id: str,
) -> Union[User, UserGetIdGetResponse, UserGetIdGetResponse1]:
    pass


@app.post(
    "/user/register",
    response_model=UserRegisterPostResponse,
    responses={
        "500": {"model": UserRegisterPostResponse1},
        "503": {"model": UserRegisterPostResponse2},
    },
)
def post_user_register(
    body: UserRegisterPostRequest = None,
) -> Union[
    UserRegisterPostResponse, UserRegisterPostResponse1, UserRegisterPostResponse2
]:
    pass


@app.get(
    "/user/search",
    response_model=List[User],
    responses={
        "500": {"model": UserSearchGetResponse},
        "503": {"model": UserSearchGetResponse1},
    },
)
def get_user_search(
    first_name: str, last_name: str = ...
) -> Union[List[User], UserSearchGetResponse, UserSearchGetResponse1]:
    pass