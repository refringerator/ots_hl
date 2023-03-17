from models import UserRegisterPostRequest
from auth import Auth
import uuid

from database import query_put, query_get

auth_handler = Auth()


def register_user(user_model: UserRegisterPostRequest):
    hashed_password = auth_handler.get_password_hash(user_model.password)
    user_id = uuid.uuid4()

    rowcount = query_put(
        """
            INSERT INTO user (
                id,
                first_name,
                second_name,
                age,
                biography,
                city,
                password_hash
                ) VALUES (%s,%s,%s,%s,%s,%s,%s)
            """,
        (
            user_id.bytes,
            user_model.first_name,
            user_model.second_name,
            user_model.age,
            user_model.biography,
            user_model.city,
            hashed_password,
        ),
    )
    return str(user_id) if rowcount else None


def get_user_by_id(user_id: str):
    uid = uuid.UUID(user_id)
    user = query_get(
        """
        SELECT 
            BIN_TO_UUID(user.id) as id,
            user.first_name,
            user.second_name,
            user.age,
            user.biography,
            user.city,
            user.password_hash
        FROM user 
        WHERE id = %s
        """,
        (uid.bytes),
    )
    return user


def authenticate_user(user_id, password):
    user = get_user_by_id(user_id)[0]
    if not user:
        return False
    if not auth_handler.verify_password(password, user["password_hash"]):
        return False
    return user
