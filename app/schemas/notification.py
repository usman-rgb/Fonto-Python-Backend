<<<<<<< HEAD
from pydantic import BaseModel

class Notification(BaseModel):
    id: int
    message: str
    user_id: int

    class Config:
=======
from pydantic import BaseModel

class Notification(BaseModel):
    id: int
    message: str
    user_id: int

    class Config:
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
        from_attributes = True  # Updated from orm_mode=True