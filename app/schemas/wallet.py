<<<<<<< HEAD
from pydantic import BaseModel

class Wallet(BaseModel):
    id: int
    user_id: int
    balance: float
    address: str

    class Config:
=======
from pydantic import BaseModel

class Wallet(BaseModel):
    id: int
    user_id: int
    balance: float
    address: str

    class Config:
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
        from_attributes = True  # Updated from orm_mode=True