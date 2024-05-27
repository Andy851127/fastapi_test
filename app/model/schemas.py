from pydantic import BaseModel
from datetime import datetime

class BlogBase(BaseModel):
    title: str
    author: str
    comment: str

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UsersBase(BaseModel):
    user_id: int
    user_name: str
    email: str

class UserCreate(UsersBase):
    pass

class Users(UsersBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
