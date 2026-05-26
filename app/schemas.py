from pydantic import BaseModel, EmailStr, Field, ConfigDict 
from datetime import datetime
from typing import Optional, Annotated

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    model_config= ConfigDict(from_attributes=True)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str  

class TokenData(BaseModel):
    id: Optional[str]=None 

class UserProfile(UserResponse):
    avatar_url: Optional[str] = None
    bio: Optional[str] = None

class UserUpdate(BaseModel):
    username: Optional[str] = None
    bio: Optional[str] = None

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    tags: Optional[list[str]] = None
    published: bool = False
    cover_image_url: Optional[str] = None

class PostDetail(PostBase):
    post_id: int
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    tags: Optional[list[str]] = None
    published: bool
    cover_image_url: Optional[str] = None

    model_config= ConfigDict(from_attributes=True)

class PostSummary(BaseModel):
    post_id: int
    title: str
    owner_username: str
    created_at: datetime

    model_config= ConfigDict(from_attributes=True)

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[list[str]] = None
    published: Optional[bool] = None
    cover_image_url: Optional[str] = None

class MessageResponse(BaseModel):
    message: str

