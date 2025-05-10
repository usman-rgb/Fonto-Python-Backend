from pydantic import BaseModel

class Wallet(BaseModel):
    id: int
    user_id: int
    balance: float
    address: str

    class Config:

from pydantic import BaseModel

class Wallet(BaseModel):
    id: int
    user_id: int
    balance: float
    address: str

    class Config:

        from_attributes = True  # Updated from orm_mode=True
