from app.api.models import ContactSchema
from app.db import contacts, database

async def post(payload: ContactSchema):
    query = contacts.insert().values(first_name=payload.first_name, last_name=payload.last_name)
    return await database.execute(query=query)

async def get(id: int):
    query = contacts.select().where(id == contacts.c.id)
    return await database.fetch_one(query=query)

async def get_all():
    query = contacts.select()
    return await database.fetch_all(query=query)

async def put(id: int, payload: ContactSchema):
    query = (
        contacts
        .update()
        .where(id == contacts.c.id)
        .values(first_name=payload.first_name, last_name=payload.last_name)
        .returning(contacts.c.id)
    )
    return await database.execute(query=query)