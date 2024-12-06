from fastapi import APIRouter
from ..models.types import User
from ..crud.user import *

router = APIRouter()

@router.get("/user", response_model=list[User])
async def findAll():
    return await get_users()

@router.get("/user/{id}", response_model=User)
async def findOne(id: int):
    return await get_user(id)

@router.post("/user", response_model=User)
async def createOne(user: User):
    return await create_user(user)

@router.put("/user/{id}", response_model=User)
async def updateOne(id: int, user: User):
    return await update_user(id, user)

@router.delete("/user/{id}", response_model=User)
async def deleteOne(id: int):
    return await delete_user(id)

@router.get("/user/{email}", response_model=User)
async def authenticate(email: str, password: str):
    return await authenticate_user(email, password)