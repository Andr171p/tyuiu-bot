from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


admin_router = APIRouter(
    prefix="/admin"
)

admin_router.mount(
    path="/static",
    app=StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(directory="templates")


@admin_router.get(path="/", response_model=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request})