from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.config import settings


admin_router = APIRouter(
    prefix="/admin"
)

static_path = settings.static.static_dir

admin_router.mount(static_path, StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@admin_router.get(path="/")
async def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request})