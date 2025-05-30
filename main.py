# main.py

from fastapi import FastAPI
from app.config.env import Config
from app.modules.routes import router
from app.pkg.middleware.error_handler import ErrorHandlerMiddleware

# App initialization ------------------------------
app = FastAPI()

# App Routes --------------------------------
app.include_router(router)

# App Middleware --------------------------------
app.add_middleware(ErrorHandlerMiddleware)