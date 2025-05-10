from pydantic import BaseModel

class Newsletter(BaseModel):

    email: str
