from fastapi import FastAPI

from models import (
    LoginPostRequest,
    LoginPostResponse,
    ErrorResponse,
    User,
    UserRegisterPostRequest,
    UserRegisterPostResponse,
)
from datetime import datetime
from auth import Auth
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uuid

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
auth_handler = Auth()

from database.query import query_get, query_put, query_update


app = FastAPI(
    title="OTUS Highload Architect",
    version="1.0.0",
)
def register_user(user_model: UserRegisterPostRequest):
    hashed_password = auth_handler.get_password_hash(user_model.password)
    user_id = uuid.uuid4()
    
    ret = query_put("""
              INSERT INTO user (
                  id,
                  first_name,
                  second_name,
                  age,
                  password_hash
                  ) VALUES (%s,%s,%s,%s,%s)
              """,
              (
                  user_id.bytes,
                  user_model.first_name,
                  user_model.second_name,
                  user_model.age,
                  hashed_password
                  )
              )
    return str(user_id)

def get_user(db, username):
    return User(
        {
            "username": "test",
            "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        }
    )

def get_user_by_id(user_id: str):
    uid = uuid.UUID(user_id)
    user = query_get("""
        SELECT 
            user.id,
            user.first_name,
            user.second_name,
            user.age
        FROM user 
        WHERE id = %s
        """, (uid.bytes))
    return user


def authenticate_user(db, username, password):
    user = get_user(db, username)
    if not user:
        return False
    if not auth_handler.verify_password(password, user.hashed_password):
        return False
    return user


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
    data = get_user_by_id(id)[0]
    data['id'] = id
    return User(**data)


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
