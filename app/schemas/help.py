from pydantic import BaseModel

class HelpQuestion(BaseModel):
    id: int
    question: str
    answer: str

    class Config:

        from_attributes = True  # Updated from orm_mode=True
