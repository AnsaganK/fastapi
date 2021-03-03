from fastapi import APIRouter
from fastapi import Body

from app.views.auth.auth_handler import signJWT
from app.models.user import User
from app.schemas.user import UserSchema, UserLoginSchema
from . import session
from app.views.user import check_user

router = APIRouter()


@router.post("/user/signup")
async def create_user(user: UserSchema = Body(...)):
    query = User(name=user.name,
                 first_name=user.first_name,
                 last_name=user.last_name,
                 email=user.email,
                 password=user.password)
    for i in session.query(User).all():
        if i.name == user.name:
            return {"error": "A user with this name has already been created"}
        if i.email == user.email:
            return {"error": "A user with this email has already been created"}

    session.add(query)
    session.commit()

    return signJWT(user.email)


@router.post("/user/login")
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }

