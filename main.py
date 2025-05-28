from fastapi import FastAPI
from app.config.env import Config

app = FastAPI()

@app.get("/")
async def root(): 
  return {
      "message": "Hello World ✨",
      "PORT: ": Config.PORT,
      "sheets_id: ": Config.GOOGLE_SHEETS_ID
    }