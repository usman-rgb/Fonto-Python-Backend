<<<<<<< HEAD
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, nullable=True)
    hashed_password = Column(String)
    nfts = relationship("NFT", back_populates="owner")
    bids = relationship("Bid", back_populates="bidder")
    wallet = relationship("Wallet", back_populates="user", uselist=False)
=======
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, nullable=True)
    hashed_password = Column(String)
    nfts = relationship("NFT", back_populates="owner")
    bids = relationship("Bid", back_populates="bidder")
    wallet = relationship("Wallet", back_populates="user", uselist=False)
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
    notifications = relationship("Notification", back_populates="user")