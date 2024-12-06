from fastapi import APIRouter, HTTPException
from ...schemas.tag import TagCreate, TagRead
from ...core.prisma import prisma

router = APIRouter()

@router.post("/tags/", response_model=TagRead)
async def create_tag(tag: TagCreate):
    created_tag = await prisma.tag.create(data=tag.dict())
    return created_tag

@router.get("/tags/{tag_id}", response_model=TagRead)
async def get_tag(tag_id: int):
    tag = await prisma.tag.find_unique(where={"id": tag_id})
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag
