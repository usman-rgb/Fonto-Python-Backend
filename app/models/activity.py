from sqlalchemy import Column, Integer, String
from app.database import Base

class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True)
    action = Column(String)

    timestamp = Column(String)
