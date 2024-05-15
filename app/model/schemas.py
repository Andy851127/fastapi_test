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
