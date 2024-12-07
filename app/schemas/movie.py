from pydantic import BaseModel
from typing import List, Optional

# Create DTO
class MovieCreate(BaseModel):
    title: str
    genres: List[str]

# Read DTO
class MovieRead(BaseModel):
    id: int
    title: str
    genres: List[str]
    avgRating: float
    ratingCount: int

    class Config:
        from_attributes = True

# Update DTO (para quando for alterar informações, como média de avaliações)
class MovieUpdate(BaseModel):
    title: Optional[str] = None
    genres: Optional[List[str]] = None
    avgRating: Optional[float] = None
    ratingCount: Optional[int] = None