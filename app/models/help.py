from sqlalchemy import Column, Integer, String
from app.database import Base

class HelpQuestion(Base):
    __tablename__ = "help_questions"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)

    answer = Column(String)
