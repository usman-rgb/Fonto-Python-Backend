from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Collection(Base):
    __tablename__ = "collections"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Collection(Base):
    __tablename__ = "collections"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)

    nfts = relationship("NFT", back_populates="collection")
