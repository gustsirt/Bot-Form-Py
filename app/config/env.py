import os
from dotenv import load_dotenv

load_dotenv()  # Carga el archivo .env automáticamente

REQUIRED_ENV_VARS = [
    "USER_ADMIN_PASS",
    "SECRET_COOKIE",
    "BASE_WP_URL",
    "API_VERSION",
    "API_TOKEN",
    "BUSINESS_PHONE",
    "WEBHOOK_VERIFY_TOKEN",
    "GOOGLE_SERVICE_ACCOUNT_EMAIL",
    "GOOGLE_PRIVATE_KEY",
    "GOOGLE_SHEETS_ID",
    "CONFIG_SHEET",
    "SESSION_SHEET",
    "ANSWERS_SHEET",
    "PENDING_SHEET",
    "CHAT_GPT_API_KEY",
    "CHAT_GPT_PROMPT",
]

# Validar variables obligatorias
missing_vars = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]
if missing_vars:
    raise EnvironmentError(f"Faltan las siguientes variables de entorno: {', '.join(missing_vars)}")
  
# Acceso limpio a las variables
class Config:
    PORT = int(os.getenv("PORT", 3000))
    USER_ADMIN_PASS = os.getenv("USER_ADMIN_PASS")
    SECRET_COOKIE = os.getenv("SECRET_COOKIE")
    NODE_ENV = os.getenv("NODE_ENV", "development")

    BASE_WP_URL = os.getenv("BASE_WP_URL")
    API_VERSION = os.getenv("API_VERSION")
    API_TOKEN = os.getenv("API_TOKEN")
    BUSINESS_PHONE = os.getenv("BUSINESS_PHONE")
    WEBHOOK_VERIFY_TOKEN = os.getenv("WEBHOOK_VERIFY_TOKEN")

    GOOGLE_SERVICE_ACCOUNT_EMAIL = os.getenv("GOOGLE_SERVICE_ACCOUNT_EMAIL")
    GOOGLE_PRIVATE_KEY = os.getenv("GOOGLE_PRIVATE_KEY")

    GOOGLE_SHEETS_ID = os.getenv("GOOGLE_SHEETS_ID")
    CONFIG_SHEET = os.getenv("CONFIG_SHEET")
    SESSION_SHEET = os.getenv("SESSION_SHEET")
    ANSWERS_SHEET = os.getenv("ANSWERS_SHEET")
    PENDING_SHEET = os.getenv("PENDING_SHEET")

    CHAT_GPT_API_KEY = os.getenv("CHAT_GPT_API_KEY")
    CHAT_GPT_PROMPT = os.getenv("CHAT_GPT_PROMPT")