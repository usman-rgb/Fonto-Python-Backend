<<<<<<< HEAD
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Collection(Base):
    __tablename__ = "collections"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
=======
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Collection(Base):
    __tablename__ = "collections"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
    nfts = relationship("NFT", back_populates="collection")