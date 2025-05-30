from app.pkg.services.google_client import get_google_sheets_client
from app.config.env import Config

# ✍️ Agrega una fila al Sheet en modo append.
def add_to_sheet(data, range_=None, spreadsheet_id=None):
  spreadsheet_id = spreadsheet_id or Config.GOOGLE_SHEETS_ID
  range_ = range_ or Config.ANSWERS_SHEET

  sheets = get_google_sheets_client()
  
  try:
      sheets.values().append(
          spreadsheetId=spreadsheet_id,
          range=range_,
          valueInputOption='RAW',
          insertDataOption='INSERT_ROWS',
          body={
              "values": [data]
          }
      ).execute()
      return "✅ Datos correctamente agregados"
  except Exception as e:
      print("❌ Error en add_to_sheet:", e)
      raise e
      
# 📖 Lee datos desde el rango indicado.
def get_from_sheet(range_, spreadsheet_id=None):
  spreadsheet_id = spreadsheet_id or Config.GOOGLE_SHEETS_ID
  sheets = get_google_sheets_client()
  
  try:
      result = sheets.values().get(
          spreadsheetId=spreadsheet_id,
          range=range_
      ).execute()
      return result.get("values", [])
  except Exception as e:
      print("❌ Error en get_from_sheet:", e)
      raise e