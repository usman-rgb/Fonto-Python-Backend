<<<<<<< HEAD
from pydantic import BaseModel

class CollectionCreate(BaseModel):
    name: str
    description: str

class Collection(BaseModel):
    id: int
    name: str
    description: str

    class Config:
=======
from pydantic import BaseModel

class CollectionCreate(BaseModel):
    name: str
    description: str

class Collection(BaseModel):
    id: int
    name: str
    description: str

    class Config:
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
        from_attributes = True  # Updated from orm_mode=True