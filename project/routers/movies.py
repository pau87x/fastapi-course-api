from fastapi import HTTPException, APIRouter
from ..database import User, Movie, UserReview
from ..schemas import MovieRequestModel, MovieResponseModel

router = APIRouter(prefix='/api/v1/movies')

@router.post('',response_model=MovieResponseModel)
async def create_movie(movie: MovieRequestModel):
    movie = Movie.create(
        title = movie.title
        )
    return movie