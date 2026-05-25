from fastapi import FastAPI

from . import models
from .database import engine
from .routers import user
from .config import settings

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(user.router)

@app.get("/")
def root(): 
    return {"message": "Welcome to my World"}
