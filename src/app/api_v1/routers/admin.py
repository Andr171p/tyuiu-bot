from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


admin_router = APIRouter(
    prefix="/admin"
)

templates = Jinja2Templates(directory="static/templates")


@admin_router.get(path="/")
async def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        name="index.html",
        context={"request": request}
    )