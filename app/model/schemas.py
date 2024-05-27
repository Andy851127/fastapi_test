from pydantic import BaseModel
from datetime import datetime

class BlogBase(BaseModel):
    title: str = '反脆弱'
    author: str = 'Andy'
    comment: str = '遇到事情的處理方式'

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UsersBase(BaseModel):
    user_id: int = 1
    user_name: str = "AndyChen"
    email: str = "andychen@gmail.com"

class UserCreate(UsersBase):
    pass

class Users(UsersBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
