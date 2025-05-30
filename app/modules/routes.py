# app/modules/router.py

from fastapi import APIRouter
from app.config.env import Config
from app.pkg.services.google_client import get_google_sheets_client
from app.pkg.services.sheet_service import get_from_sheet, add_to_sheet

router = APIRouter()

@router.get("/")
async def root(): 
    return {
        "message": "Hello World ✨",
        "PORT": Config.PORT,
        "sheets_id": Config.GOOGLE_SHEETS_ID
    }

@router.get("/sheet-data")
async def read_sheet_raw():
    sheet = get_google_sheets_client()
    result = sheet.values().get(
        spreadsheetId=Config.GOOGLE_SHEETS_ID,
        range=Config.CONFIG_SHEET
    ).execute()
    values = result.get("values", [])
    return {"rows": values}

@router.get("/sheet")
async def read_sheet():
    values = get_from_sheet("TPREGUNTAS")
    return {"data": values}

@router.post("/sheet")
async def write_sheet():
    new_row = ["Juan", "Pérez", "juan@mail.com"]
    message = add_to_sheet(new_row)
    return {"message": message}