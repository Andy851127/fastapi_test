from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/blogs/", response_model=schemas.Blog)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(database.get_db)):
    return crud.create_blog(db=db, blog=blog)

@app.get("/blogs/", response_model=list[schemas.Blog])
def read_blogs(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    blogs = crud.get_blogs(db, skip=skip, limit=limit)
    return blogs

@app.get("/blogs/{blog_id}", response_model=schemas.Blog)
def read_blog(blog_id: int, db: Session = Depends(database.get_db)):
    db_blog = crud.get_blog(db, blog_id=blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog

@app.put("/blogs/{blog_id}", response_model=schemas.Blog)
def update_blog(blog_id: int, blog: schemas.BlogCreate, db: Session = Depends(database.get_db)):
    db_blog = crud.update_blog(db, blog_id=blog_id, blog=blog)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog

@app.delete("/blogs/{blog_id}", response_model=schemas.Blog)
def delete_blog(blog_id: int, db: Session = Depends(database.get_db)):
    db_blog = crud.delete_blog(db, blog_id=blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog
