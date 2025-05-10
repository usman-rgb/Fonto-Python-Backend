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

        from_attributes = True  # Updated from orm_mode=True
