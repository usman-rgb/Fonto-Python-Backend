<<<<<<< HEAD
from sqlalchemy import Column, Integer, String
from app.database import Base

class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True)
    action = Column(String)
=======
from sqlalchemy import Column, Integer, String
from app.database import Base

class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True)
    action = Column(String)
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
    timestamp = Column(String)