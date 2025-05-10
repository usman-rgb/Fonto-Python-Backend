<<<<<<< HEAD
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
=======
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
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
    email: EmailStr