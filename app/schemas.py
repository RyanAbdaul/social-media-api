from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, Literal

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    email: EmailStr
    id: int
    created_at: datetime
    class Config:
        orm_mode = True
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True 
    
class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id          : int
    user        : UserOut
    created_at  : datetime


    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token : str
    token_type : str
    
class TokenData(BaseModel):
    id : int
    
class Like(BaseModel):
    post_id : int
    dir : Literal[0, 1]