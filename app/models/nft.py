from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class NFT(Base):
    __tablename__ = "nfts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    ipfs_hash = Column(String)
    xrpl_token_id = Column(String, nullable=True)
    collection_id = Column(Integer, ForeignKey("collections.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="nfts")
    collection = relationship("Collection", back_populates="nfts")

    bids = relationship("Bid", back_populates="nft")
