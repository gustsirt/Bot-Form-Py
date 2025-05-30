from fastapi import FastAPI
from app.config.env import Config
from app.modules.routes import router

app = FastAPI()

app.include_router(router)