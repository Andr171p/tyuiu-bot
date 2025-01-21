from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.config import settings


static_path = str(settings.static.static_dir)
template_path = str(settings.static.template_dir)

admin_router = APIRouter(
    prefix="/admin"
)

admin_router.mount(static_path, StaticFiles(directory=static_path), name="static")

templates = Jinja2Templates(directory=template_path)


@admin_router.get(path="/")
async def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request})