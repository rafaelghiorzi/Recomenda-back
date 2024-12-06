from ..models.types import User
from ..utils.prisma import prisma

async def get_user(id: int):
    try:
        user = await prisma.user.find_unique(where={"id": id})
        if user:
            return User(**user.model_dump())
    except Exception as e:
        return {"error": str(e)}
    
async def create_user(user: User):
    try:
        user = await prisma.user.create(data=user.model_dump())
        return User(**user.model_dump())
    except Exception as e:
        return {"error": str(e)}
    
async def get_users():
    try:
        users = await prisma.user.find_many()
        return [User(**user.model_dump()) for user in users]
    except Exception as e:
        return {"error": str(e)}
    
async def update_user(id: int, user: User):
    try:
        user = await prisma.user.update(where={"id": id}, data=user.model_dump())
        return User(**user.model_dump())
    except Exception as e:
        return {"error": str(e)}
    
async def delete_user(id: int):
    try:
        user = await prisma.user.delete(where={"id": id})
        return User(**user.model_dump())
    except Exception as e:
        return {"error": str(e)}

def authenticate_user(email: str, password: str):
    try:
        user = prisma.user.find_unique(where={"email": email})
        if not user and user.password == password:
            return False
        if not user:
            return False
        return user
    except Exception as e:
        return {"error": str(e)}
