from pydantic import BaseModel
from datetime import datetime

# Create DTO
class TagCreate(BaseModel):
    userId: int
    movieId: int
    tag: str

# Read DTO
class TagRead(BaseModel):
    id: int
    userId: int
    movieId: int
    tag: str
    createdAt: datetime

    class Config:
        orm_mode = True