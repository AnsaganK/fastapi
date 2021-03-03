from pydantic import BaseModel, Field, EmailStr

#class UserBaseSchema(BaseModel):
#    pass


class UserSchema(BaseModel):
    name: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Ka An Or",
                "first_name": "Ka An Or",
                "last_name": "Ka An Or",
                "email": "ansagankabdolla4@gmail.com",
                "password": "12345",
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example":{
                "email": "ansagankabdolla4@gmail.com",
                "password":"12345"
            }
        }
