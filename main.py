from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

app = FastAPI()

@app.get("/")
async def root(): 
  PORT = os.getenv("PORT", "Port not found")
  return {"message": "Hello World ✨", "PORT: ": PORT}