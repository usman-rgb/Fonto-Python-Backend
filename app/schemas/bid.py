<<<<<<< HEAD
from pydantic import BaseModel

class BidCreate(BaseModel):
    nft_id: int
    amount: float

class Bid(BaseModel):
    id: int
    nft_id: int
    bidder_id: int
    amount: float

    class Config:
=======
from pydantic import BaseModel

class BidCreate(BaseModel):
    nft_id: int
    amount: float

class Bid(BaseModel):
    id: int
    nft_id: int
    bidder_id: int
    amount: float

    class Config:
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
        from_attributes = True  # Updated from orm_mode=True