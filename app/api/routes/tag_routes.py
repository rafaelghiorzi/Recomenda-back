from fastapi import APIRouter, Depends, HTTPException, status
from ...schemas.tag import TagCreate, TagRead
from ...core.prisma import prisma

router = APIRouter()

@router.post("", response_model=TagRead, status_code=status.HTTP_201_CREATED)
async def create(tag: TagCreate):
    try:
        # Create new tag
        created_tag = await prisma.tag.create(data=tag.model_dump())
        return created_tag
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=list[TagRead])
async def findAll():
    try:
        # List all tags
        tags = await prisma.tag.find_many()
        if not tags:
            raise HTTPException(status_code=404, detail="Tags not found")
        return tags
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{tag_id}", response_model=TagRead)
async def findOne(tag_id: int):
    try:
        # Find tag by ID
        tag = await prisma.tag.find_unique(where={"id": tag_id})
        if not tag:
            raise HTTPException(status_code=404, detail="Tag not found")
        return tag
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{tag_id}", response_model=TagRead)
async def update():
    raise HTTPException(status_code=501, detail="You can't update a tag")

@router.delete("/{tag_id}", response_model=TagRead)
async def delete(tag_id: int):
    try:
        # Delete tag
        deleted_tag = await prisma.tag.delete(where={"id": tag_id})
        if not deleted_tag:
            raise HTTPException(status_code=404, detail="Tag not found")
        return deleted_tag
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))