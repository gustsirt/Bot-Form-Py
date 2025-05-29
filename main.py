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


# @app.get("/sheet")
# async def read_sheet():
#     values = get_from_sheet("TPREGUNTAS")  # o tu Config.CONFIG_SHEET
#     return {"data": values}

# @app.post("/sheet")
# async def write_sheet():
#     new_row = ["Juan", "Pérez", "juan@mail.com"]  # simulado
#     message = add_to_sheet(new_row)
#     return {"message": message}