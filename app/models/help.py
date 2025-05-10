<<<<<<< HEAD
from sqlalchemy import Column, Integer, String
from app.database import Base

class HelpQuestion(Base):
    __tablename__ = "help_questions"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
=======
from sqlalchemy import Column, Integer, String
from app.database import Base

class HelpQuestion(Base):
    __tablename__ = "help_questions"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
    answer = Column(String)