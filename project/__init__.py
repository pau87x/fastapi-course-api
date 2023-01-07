from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from .database import database as connection
from .database import User, Movie, UserReview

from .routers import user_router
from .routers import review_router
from .routers import movie_router

app = FastAPI(title='A little IMDB',
             description='With this project movies can be reviewed',
             version='1.0')

api_v1 = APIRouter(prefix='/api/v1')

api_v1.include_router(user_router)
api_v1.include_router(review_router)
api_v1.include_router(movie_router)

@api_v1.post('/auth')
async def auth(data: OAuth2PasswordRequestForm = Depends()):
    user = User.authenticate(data.username, data.password)
    if user:
        return {
            'username': data.username,
            'password': data.password
        }
    else:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Usuario o password incorrectos',
                headers={'www-Autenticate': 'Beraer' }
            )

app.include_router(api_v1)

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
        print('Starting server... connecting to db')

    connection.create_tables([User, Movie, UserReview])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close
        print('Shutdown server... closing connection')

