# app/modules/routes/views.py

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Motor de Plantillas --------------------------------
templates = Jinja2Templates(directory="app/pages")

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home_view(request: Request):
  return templates.TemplateResponse("index.html", {
    "request": request,
    "title": "Inicio",
    "message": "Bienvenido al bot 🚀"
  })
