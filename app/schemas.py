from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, time


class User(BaseModel):
    email: EmailStr 
    password: str
    class Config:
        orm_mode = True


class NewUserResponse(BaseModel):
    email: EmailStr
    user_id: int



    

    