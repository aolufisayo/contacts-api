import os
from databases import Database
from sqlalchemy import (Column, DateTime, Integer, String, Table, create_engine, MetaData)
from sqlalchemy.sql import func

DATABASE_URL = os.getenv("DATABASE_URL")

#SQLALCHEMY
engine = create_engine(DATABASE_URL)
metadata = MetaData()
contacts = Table(
    "contacts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String(50)),
    Column("last_name", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

#database query builder
database = Database(DATABASE_URL)