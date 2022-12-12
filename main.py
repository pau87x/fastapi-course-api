from fastapi import FastAPI 
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
    user = User.create(
        username = user.username, 
        password = user.password
    )
    return user.id