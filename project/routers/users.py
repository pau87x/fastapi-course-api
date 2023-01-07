from typing import List
from fastapi import HTTPException, APIRouter, Response, Cookie, Depends
from fastapi.security import HTTPBasicCredentials

from ..common import oauth2_schema, get_current_user

from ..database import User
from ..schemas import UserRequestModel, UserResponseModel, ReviewResponseModel

router = APIRouter(prefix='/users')

@router.post('',response_model=UserResponseModel)
async def create_user(user: UserRequestModel):
    if User.select().where(User.username == user.username).exists():
        raise HTTPException(409, 'El username se encuentra en uso')
    hash_password = User.create_password(user.password)

    user = User.create(
        username = user.username, 
        password = hash_password
    )

    return user

@router.post('/login', response_model=UserResponseModel)
async def login(credentials: HTTPBasicCredentials, response: Response):
    user = User.select().where(User.username == credentials.username).first()

    if user is None:
        raise HTTPException(409, 'Usuario no encontrado')

    if user.password != User.create_password(credentials.password):
        raise HTTPException(404, 'Password error')

    response.set_cookie(key='user_id', value=user.id)
    return user

@router.get('/reviews')
async def get_reviews(user: User = Depends(get_current_user)):
    return {
        'id': user.id,
        'username': user.username
    }


