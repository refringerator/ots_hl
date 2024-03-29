from typing import Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    id: Optional[str] = Field(None, description="Идентификатор пользователя")
    first_name: Optional[str] = Field(None, description="Имя", example="Имя")
    second_name: Optional[str] = Field(None, description="Фамилия", example="Фамилия")
    age: Optional[int] = Field(None, description="Возраст", example=18)
    biography: Optional[str] = Field(
        None, description="Интересы", example="Хобби, интересы и т.п."
    )
    city: Optional[str] = Field(None, description="Город", example="Москва")


class LoginPostRequest(BaseModel):
    id: Optional[str] = Field(None, example="234")
    password: Optional[str] = Field(None, example="Секретная строка")


class LoginPostResponse(BaseModel):
    token: Optional[str] = Field(None, example="e4d2e6b0-cde2-42c5-aac3-0b8316f21e58")


class ErrorResponse(BaseModel):
    message: str = Field(..., description="Описание ошибки")
    request_id: Optional[str] = Field(
        None,
        description="Идентификатор запроса. Предназначен для более быстрого поиска проблем.",
    )
    code: Optional[int] = Field(
        None,
        description="Код ошибки. Предназначен для классификации проблем и более быстрого решения проблем.",
    )


class UserRegisterPostRequest(BaseModel):
    first_name: Optional[str] = Field(None, example="Имя")
    second_name: Optional[str] = Field(None, example="Фамилия")
    age: Optional[int] = Field(None, example=18)
    biography: Optional[str] = Field(None, example="Хобби, интересы и т.п.")
    city: Optional[str] = Field(None, example="Москва")
    password: Optional[str] = Field(None, example="Секретная строка")


class UserRegisterPostResponse(BaseModel):
    user_id: Optional[str] = Field(None, example="e4d2e6b0-cde2-42c5-aac3-0b8316f21e58")
