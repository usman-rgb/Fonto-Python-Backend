from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    username: str = None

class UserBase(BaseModel):
    email: EmailStr
    username: str = None

class User(UserBase):
    id: int

    class Config:
        from_attributes = True  # Updated from orm_mode=True

class Token(BaseModel):
    access_token: str
    token_type: str

class PasswordResetRequest(BaseModel):

    email: EmailStr
