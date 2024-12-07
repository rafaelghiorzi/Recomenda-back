from fastapi import APIRouter, Depends, HTTPException, status
from typing import Optional
from ...schemas.user import UserCreate, UserRead, UserUpdate
from ...core.prisma import prisma
from ...core.auth import get_current_user
router = APIRouter()

@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create(user: UserCreate = Depends(get_current_user)):
    try:
        # Criar novo usuário
        user = await prisma.user.create(data={
            "username": user.username,
            "email": user.email,
            "password": user.password
        })
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=list[UserRead])
async def findAll(current_user: UserRead = Depends(get_current_user)):
    try:
        # Listar todos os usuários
        users = await prisma.user.find_many()
        if not users:
            raise HTTPException(status_code=404, detail="Users not found")
        return users
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=UserRead)
async def findOne(user_id: int = Depends(get_current_user)):
    try:
        # Buscar usuário pelo ID
        user = await prisma.user.find_unique(where={"id": user_id})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{user_id}", response_model=UserRead)
async def update(user_id: int, user: UserUpdate = Depends(get_current_user)):
    try:
        # Atualizar usuário
        updated_user = await prisma.user.update(
            where={"id": user_id},
            data=user.model_dump(exclude_unset=True)  # Atualizar apenas os campos passados
        )
        return updated_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/{user_id}", response_model=UserRead)
async def delete(user_id: int = Depends(get_current_user)):
    try:
        # Deletar usuário
        deleted_user = await prisma.user.delete(where={"id": user_id})
        if not deleted_user:
            raise HTTPException(status_code=404, detail="User not found")
        return deleted_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))