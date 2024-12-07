from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Create DTO
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Read DTO (com retorno mais completo)
class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True

# Update DTO
class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    

# Token DTO
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str