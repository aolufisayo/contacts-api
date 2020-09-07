from app.api import crud
from app.api.models import ContactSchema, ContactDB
from fastapi import APIRouter
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