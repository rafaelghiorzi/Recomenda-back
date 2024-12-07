from fastapi import APIRouter, Depends, HTTPException, status
from ...schemas.rating import RatingCreate, RatingRead
from ...core.prisma import prisma

router = APIRouter()

@router.post("", response_model=RatingRead, status_code=status.HTTP_201_CREATED)
async def create(rating: RatingCreate):
    try:
        # Create new rating
        created_rating = await prisma.rating.create(data=rating.model_dump())
        return created_rating
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=list[RatingRead])
async def findAll():
    try:
        # List all ratings
        ratings = await prisma.rating.find_many()
        if not ratings:
            raise HTTPException(status_code=404, detail="Ratings not found")
        return ratings
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{rating_id}", response_model=RatingRead)
async def findOne(rating_id: int):
    try:
        # Find rating by ID
        rating = await prisma.rating.find_unique(where={"id": rating_id})
        if not rating:
            raise HTTPException(status_code=404, detail="Rating not found")
        return rating
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{rating_id}", response_model=RatingRead)
async def update():
    raise HTTPException(status_code=501, detail="You can't update a rating")

@router.delete("/{rating_id}", response_model=RatingRead)
async def delete(rating_id: int):
    try:
        # Delete rating
        deleted_rating = await prisma.rating.delete(where={"id": rating_id})
        if not deleted_rating:
            raise HTTPException(status_code=404, detail="Rating not found")
        return deleted_rating
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))