<<<<<<< HEAD
from sqlalchemy import Column, Integer, String
from app.database import Base

class Newsletter(Base):
    __tablename__ = "newsletters"
    id = Column(Integer, primary_key=True, index=True)
=======
from sqlalchemy import Column, Integer, String
from app.database import Base

class Newsletter(Base):
    __tablename__ = "newsletters"
    id = Column(Integer, primary_key=True, index=True)
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
    email = Column(String, unique=True, index=True)