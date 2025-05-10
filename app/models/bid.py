from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Bid(Base):
    __tablename__ = "bids"
    id = Column(Integer, primary_key=True, index=True)
    nft_id = Column(Integer, ForeignKey("nfts.id"))
    bidder_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)
    nft = relationship("NFT", back_populates="bids")

from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Bid(Base):
    __tablename__ = "bids"
    id = Column(Integer, primary_key=True, index=True)
    nft_id = Column(Integer, ForeignKey("nfts.id"))
    bidder_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)
    nft = relationship("NFT", back_populates="bids")

    bidder = relationship("User", back_populates="bids")
