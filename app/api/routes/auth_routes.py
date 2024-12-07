from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from ...core.auth import hash_password, verify_password, create_access_token, create_refresh_token ,decode_access_token
from ...schemas.user import Token, UserCreate, UserRead
from ...core.prisma import prisma
from ...core.auth import oauth2_scheme

router = APIRouter()

# Criar usuário e retornar token de acesso  
@router.post("/signup", response_model=UserRead)
async def signup(user: UserCreate):
    try:
        existing_user = await prisma.user.find_unique(where={"email": user.email})
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        hashed_password = hash_password(user.password)
        new_user = await prisma.user.create(
            data={
                "username": user.username,
                "email": user.email,
                "password": hashed_password,
            }
        )
        if not new_user:
            raise HTTPException(status_code=500, detail="Failed to create user")
        return new_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/signin", response_model=Token)
async def signin(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await prisma.user.find_unique(where={"email": form_data.username})
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.email})
    refresh_token = create_refresh_token(data={"sub": user.email})
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,	
        "token_type": "bearer"
        }


@router.post("/refresh", response_model=Token)
async def refresh(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token = create_access_token(data={"sub": payload.get("sub")})
    refresh_token = create_refresh_token(data={"sub": payload.get("sub")})
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }