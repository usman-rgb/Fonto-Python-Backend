from pydantic import BaseModel

class Blog(BaseModel):
    id: int
    title: str
    content: str

    class Config:

from pydantic import BaseModel

class Blog(BaseModel):
    id: int
    title: str
    content: str

    class Config:

        from_attributes = True  # Updated from orm_mode=True
