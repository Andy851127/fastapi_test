from sqlalchemy.orm import Session
from . import models, schemas

class Blog:
    @staticmethod
    def get_blog(db: Session, blog_id: int):
        return db.query(models.Blog).filter(models.Blog.id == blog_id).first()

    @staticmethod
    def get_blogs(db: Session, skip: int = 0, limit: int = 10):
        return db.query(models.Blog).offset(skip).limit(limit).all()

    @staticmethod
    def create_blog(db: Session, blog: schemas.BlogCreate):
        db_blog = models.Blog(**blog.dict())
        db.add(db_blog)
        db.commit()
        db.refresh(db_blog)
        return db_blog

    @staticmethod
    def update_blog(db: Session, blog_id: int, blog: schemas.BlogCreate):
        db_blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
        if db_blog:
            for key, value in blog.dict().items():
                setattr(db_blog, key, value)
            db.commit()
            db.refresh(db_blog)
        return db_blog

    @staticmethod
    def delete_blog(db: Session, blog_id: int):
        db_blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
        if db_blog:
            db.delete(db_blog)
            db.commit()
        return db_blog

class Users:
    @staticmethod
    def get_user(db: Session, user_id: int):
        return db.query(models.Users).filter(models.Users.user_id == user_id).first()

    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 10):
        return db.query(models.Users).offset(skip).limit(limit).all()

    @staticmethod
    def create_user(db: Session, user: schemas.UserCreate):
        db_user = models.Users(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def update_user(db: Session, user_id: int, user: schemas.UserCreate):
        db_user = db.query(models.Users).filter(models.Users.user_id == user_id).first()
        if db_user:
            for key, value in user.dict().items():
                setattr(db_user, key, value)
            db.commit()
            db.refresh(db_user)
        return db_user

    @staticmethod
    def delete_user(db: Session, user_id: int):
        db_user = db.query(models.Users).filter(models.Users.user_id == user_id).first()
        if db_user:
            db.delete(db_user)
            db.commit()
        return db_user
