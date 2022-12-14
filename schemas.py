from pydantic import BaseModel, validator

class UserBaseModel(BaseModel):
    username: str 
    password: str

    @validator('username')
    def username_validator(cls, username):
        if len(username) < 4 or len(username)>50:
            raise ValueError('Longitud debe estar entre 3 y 50 caracteres')

        return username

class UserResponseModel(BaseModel):
    id: int
    username: str