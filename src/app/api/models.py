from pydantic import BaseModel, Field

class ContactSchema(BaseModel):
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)

class ContactDB(ContactSchema):
    id: int