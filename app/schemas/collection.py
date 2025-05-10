from pydantic import BaseModel

class CollectionCreate(BaseModel):
    name: str
    description: str

class Collection(BaseModel):
    id: int
    name: str
    description: str

    class Config:

from pydantic import BaseModel

class CollectionCreate(BaseModel):
    name: str
    description: str

class Collection(BaseModel):
    id: int
    name: str
    description: str

    class Config:

        from_attributes = True  # Updated from orm_mode=True
