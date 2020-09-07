from fastapi import FastAPI
from app.db import engine, metadata, database
from app.api import contacts

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(contacts.router, prefix="/contacts", tags=["contacts"])