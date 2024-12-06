from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List

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
        orm_mode = True

# Update DTO
class UserUpdate(BaseModel):
    username: str
    email: EmailStr