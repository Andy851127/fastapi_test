from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, database

router = APIRouter(
    prefix="/blogs",
    tags=["blogs"],
)

@router.post("/blogs/", response_model=schemas.Blog)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(database.get_db)):
    return crud.Blog.create_blog(db=db, blog=blog)

@router.get("/blogs/", response_model=list[schemas.Blog])
def read_blogs(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    blogs = crud.Blog.get_blogs(db, skip=skip, limit=limit)
    return blogs

@router.get("/blogs/{blog_id}", response_model=schemas.Blog)
def get_blog(blog_id: int, db: Session = Depends(database.get_db)):
    db_blog = crud.Blog.get_blog(db, blog_id=blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog

@router.put("/blogs/{blog_id}", response_model=schemas.Blog)
def update_blog(blog_id: int, blog: schemas.BlogCreate, db: Session = Depends(database.get_db)):
    db_blog = crud.Blog.update_blog(db, blog_id=blog_id, blog=blog)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog

@router.delete("/blogs/{blog_id}", response_model=schemas.Blog)
def delete_blog(blog_id: int, db: Session = Depends(database.get_db)):
    db_blog = crud.Blog.delete_blog(db, blog_id=blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog
