from fastapi import FastAPI
from .routers import blog
from .database import engine
from . import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
