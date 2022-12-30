
from fastapi import FastAPI, APIRouter
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
