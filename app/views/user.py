from app.schemas.user import UserLoginSchema
from app.api.v1.endpoints import session
from app.models.user import User


def check_user(data: UserLoginSchema):
    for user in session.query(User).all():
        if user.email == data.email and user.password == data.password:
            return True
    return False
