from fastapi import FastAPI
from .routers import blog
from .database import engine
from . import models
from .logging_middleware import LoggingMiddleware

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# 添加日志中间件
app.add_middleware(LoggingMiddleware)

app.include_router(blog.router)
