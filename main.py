from fastapi import FastAPI, HTTPException
from database import database as connection
from database import User, Movie, UserReview
from schemas import UserBaseModel

app = FastAPI(title='A little IMDB',
             description='With this project movies can be reviewed',
             version='1.0')

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

@app.get('/')
async def index():
    return 'hello world'

@app.post('/users')
async def create_user(user: UserBaseModel):
    if User.select().where(User.username == user.username).exists():
        return HTTPException(409, 'El username se encuentra en uso')
    hash_password = User.create_password(user.password)

    user = User.create(
        username = user.username, 
        password = hash_password
    )

    return {
        'id': user.id,
        'username': user.username
    }