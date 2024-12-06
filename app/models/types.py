from pydantic import BaseModel
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str | None = None

class Rating(BaseModel):
    id: int
    userId: int
    movieId: int
    score: float
    createdAt: datetime
    
class Tag(BaseModel):
    id: int
    userId: int
    movieId: int
    tag: str
    createdAt: datetime
    
class GenomeScore(BaseModel):
    id: int
    movieId: int
    tagId: int
    relevance: float
    
class GenomeTag(BaseModel):
    id: int
    tag: str
    scores: list[GenomeScore]
    
class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    createdAt: datetime
    updatedAt: datetime
    tags: list[Tag]
    ratings: list[Rating]
    
class Movie(BaseModel):
    id: int
    title: str
    imdbId: str
    tmdbId: str
    genres: list[str]
    ratings: list[Rating]
    tags: list[Tag]
    genome: list[GenomeScore]