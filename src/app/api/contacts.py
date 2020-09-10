from app.api import crud
from app.api.models import ContactSchema, ContactDB
from fastapi import APIRouter, HTTPException, Path
from typing import List

router = APIRouter()

@router.post("/", response_model=ContactDB, status_code=201)
async def new_contact(payload: ContactSchema):
    id = await crud.post(payload)

    response_object = {
        "id": id,
        "first_name": payload.first_name,
        "last_name": payload.last_name
    }
    return response_object

@router.get("/{id}/", response_model=ContactDB)
async def read_contact(id: int = Path(..., gt=0),):
    contact = await crud.get(id)
    if not contact:
        raise HTTPException(status_code= 404, detail="Contact Not Found")
    return contact

