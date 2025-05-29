from fastapi import FastAPI
from app.config.env import Config

from app.pkg.services.google_client import get_google_sheets_client

app = FastAPI()

@app.get("/")
async def root(): 
  return {
      "message": "Hello World ✨",
      "PORT: ": Config.PORT,
      "sheets_id: ": Config.GOOGLE_SHEETS_ID
    }

@app.get("/sheet-data")
async def read_sheet():
  sheet = get_google_sheets_client()
  result = sheet.values().get(
      spreadsheetId=Config.GOOGLE_SHEETS_ID,
      range=Config.CONFIG_SHEET
    ).execute()
  
  values = result.get("values", [])
  return {"rows": values}