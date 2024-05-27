from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..model import schemas, crud, database

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/users/", response_model=schemas.Users)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.Users.create_user(db=db, user=user)

@router.get("/users/", response_description = "所有的 users 資料", response_model=list[schemas.Users])
def get_all_users(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    users = crud.Users.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=schemas.Users)
def get_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user = crud.Users.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return db_user

@router.put("/users/{user_id}", response_model=schemas.Users)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.Users.update_user(db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return db_user

@router.delete("/users/{user_id}", response_model=schemas.Users)
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user = crud.Users.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return db_user
