from fastapi import HTTPException, APIRouter
from ..database import User
from ..schemas import UserRequestModel, UserResponseModel

router = APIRouter(prefix='/api/v1/users')

@router.post('',response_model=UserResponseModel)
async def create_user(user: UserRequestModel):
    if User.select().where(User.username == user.username).exists():
        return HTTPException(409, 'El username se encuentra en uso')
    hash_password = User.create_password(user.password)

    user = User.create(
        username = user.username, 
        password = hash_password
    )

    return user