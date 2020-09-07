from app.api.models import ContactSchema
from app.db import contacts, database

async def post(payload: ContactSchema):
    query = contacts.insert().values(first_name=payload.first_name, last_name=payload.last_name)
    return await database.execute(query=query)