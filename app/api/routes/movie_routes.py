from fastapi import APIRouter, HTTPException
from ...schemas.movie import MovieCreate, MovieRead, MovieUpdate
from ...core.prisma import prisma

router = APIRouter()

@router.post("/movies/", response_model=MovieRead)
async def create_movie(movie: MovieCreate):
    created_movie = await prisma.movie.create(data=movie.dict())
    return created_movie

@router.get("/movies/{movie_id}", response_model=MovieRead)
async def get_movie(movie_id: int):
    movie = await prisma.movie.find_unique(where={"id": movie_id})
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.put("/movies/{movie_id}", response_model=MovieRead)
async def update_movie(movie_id: int, movie: MovieUpdate):
    updated_movie = await prisma.movie.update(
        where={"id": movie_id},
        data=movie.dict(exclude_unset=True)  # Atualizar apenas os campos passados
    )
    return updated_movie
