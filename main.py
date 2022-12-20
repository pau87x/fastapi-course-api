from typing import List
from fastapi import FastAPI, HTTPException
from database import database as connection
from database import User, Movie, UserReview
from schemas import UserRequestModel, UserResponseModel
from schemas import ReviewRequestModel, ReviewResponseModel
from schemas import MovieRequestModel, MovieResponseModel

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

@app.post('/users',response_model=UserResponseModel)
async def create_user(user: UserRequestModel):
    if User.select().where(User.username == user.username).exists():
        return HTTPException(409, 'El username se encuentra en uso')
    hash_password = User.create_password(user.password)

    user = User.create(
        username = user.username, 
        password = hash_password
    )

    return user

@app.get('/reviews', response_model=List[ReviewResponseModel])
async def get_reviews():
    reviews = UserReview.select()

    return [user_review for user_review in reviews]

@app.post('/reviews',response_model=ReviewResponseModel)
async def create_review(user_review: ReviewRequestModel):
    if User.select().where(User.id == user_review.user_id).first() is None:
        raise HTTPException(404, 'El usuario no fue encontrado')

    if Movie.select().where(Movie.id == user_review.movie_id).first() is None:
        raise HTTPException(404, 'La pelicula no fue encontrada')

    user_review = UserReview.create(
        user_id = user_review.user_id,
        movie_id = user_review.movie_id,
        review = user_review.review,
        score = user_review.score
        )
    return user_review

@app.post('/movies',response_model=MovieResponseModel)
async def create_movie(movie: MovieRequestModel):
    movie = Movie.create(
        title = movie.title
        )
    return movie