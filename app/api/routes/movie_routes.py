from fastapi import APIRouter, HTTPException, status
from ...schemas.movie import MovieCreate, MovieRead, MovieUpdate
from ...core.prisma import prisma

router = APIRouter()

@router.post("", response_model=MovieRead, status_code=status.HTTP_201_CREATED)
async def create(movie: MovieCreate):
    try:
        # Create new movie
        created_movie = await prisma.movie.create(data=movie.model_dump())
        return created_movie
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=list[MovieRead])
async def findAll():
    try:
        # List all movies
        movies = await prisma.movie.find_many()
        if not movies:
            raise HTTPException(status_code=404, detail="Movies not found")
        return movies
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{movie_id}", response_model=MovieRead)
async def findOne(movie_id: int):
    try:
        # Find movie by ID
        movie = await prisma.movie.find_unique(where={"id": movie_id})
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        return movie
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{movie_id}", response_model=MovieRead)
async def update(movie_id: int, movie: MovieUpdate):
    try:
        # Update movie
        updated_movie = await prisma.movie.update(
            where={"id": movie_id},
            data=movie.model_dump(exclude_unset=True)  # Update only the passed fields
        )
        return updated_movie
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{movie_id}", response_model=MovieRead)
async def delete(movie_id: int):
    try:
        # Delete movie
        deleted_movie = await prisma.movie.delete(where={"id": movie_id})
        if not deleted_movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        return deleted_movie
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))