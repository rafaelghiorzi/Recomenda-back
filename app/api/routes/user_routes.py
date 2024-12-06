from fastapi import APIRouter, Depends, HTTPException
from ...schemas.user import UserCreate, UserRead, UserUpdate
from ...core.prisma import prisma

router = APIRouter()

@router.post("/users/", response_model=UserRead)
async def create_user(user: UserCreate):
    # Criação do usuário no banco de dados
    created_user = await prisma.user.create(data=user.model_dump())
    return created_user

@router.get("/users/{user_id}", response_model=UserRead)
async def get_user(user_id: int):
    user = await prisma.user.find_unique(where={"id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=UserRead)
async def update_user(user_id: int, user: UserUpdate):
    updated_user = await prisma.user.update(
        where={"id": user_id},
        data=user.model_dump(exclude_unset=True)  # Excluir campos não passados
    )
    return updated_user