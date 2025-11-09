from fastapi import FastAPI

from app.dependencies import create_db_and_tables
from app.models import posts
from app.routers import posts

app = FastAPI()

app.include_router(posts.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
