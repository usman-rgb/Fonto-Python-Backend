from pydantic import BaseModel

class NFTCreate(BaseModel):
    name: str
    description: str
    collection_id: int

class NFT(BaseModel):
    id: int
    name: str
    description: str
    ipfs_hash: str
    xrpl_token_id: str = None
    collection_id: int
    owner_id: int

    class Config:

        from_attributes = True  # Updated from orm_mode=True
