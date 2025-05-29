import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from app.config.env import Config

# Se define cliente de Google
def get_google_sheets_client():
    
  service_account_info = {
    "type": "service_account",
    "private_key": Config.GOOGLE_PRIVATE_KEY,
    "client_email": Config.GOOGLE_SERVICE_ACCOUNT_EMAIL,
    "token_uri": "https://oauth2.googleapis.com/token"
  }
  
  credentials = service_account.Credentials.from_service_account_info(
    service_account_info,
    scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
  )
  
  service = build("sheets", "v4", credentials=credentials)
  return service.spreadsheets()