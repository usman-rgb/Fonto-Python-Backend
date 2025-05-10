from pydantic import BaseModel

class Activity(BaseModel):
    id: int
    action: str
    timestamp: str

    class Config:

        from_attributes = True  # Updated from orm_mode=True
