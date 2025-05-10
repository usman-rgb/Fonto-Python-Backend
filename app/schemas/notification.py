from pydantic import BaseModel

class Notification(BaseModel):
    id: int
    message: str
    user_id: int

    class Config:

from pydantic import BaseModel

class Notification(BaseModel):
    id: int
    message: str
    user_id: int

    class Config:

        from_attributes = True  # Updated from orm_mode=True
