from sqlalchemy import Column, Integer, String
from app.database import Base

class Newsletter(Base):
    __tablename__ = "newsletters"
    id = Column(Integer, primary_key=True, index=True)

from sqlalchemy import Column, Integer, String
from app.database import Base

class Newsletter(Base):
    __tablename__ = "newsletters"
    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True)
