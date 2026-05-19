from pydantic import BaseModel, EmailStr, Field 
from datetime import datetime
from typing import Optional, Annotated

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str


