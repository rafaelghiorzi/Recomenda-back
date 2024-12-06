from fastapi import APIRouter, HTTPException
from ...schemas.rating import RatingCreate, RatingRead
from ...core.prisma import prisma

router = APIRouter()

@router.post("/ratings/", response_model=RatingRead)
async def create_rating(rating: RatingCreate):
    created_rating = await prisma.rating.create(data=rating.dict())
    return created_rating

@router.get("/ratings/{rating_id}", response_model=RatingRead)
async def get_rating(rating_id: int):
    rating = await prisma.rating.find_unique(where={"id": rating_id})
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    return rating
