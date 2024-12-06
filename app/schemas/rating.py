from pydantic import BaseModel

# Create DTO
class RatingCreate(BaseModel):
    userId: int
    movieId: int
    score: float

# Read DTO
class RatingRead(BaseModel):
    id: int
    userId: int
    movieId: int
    score: float

    class Config:
        orm_mode = True