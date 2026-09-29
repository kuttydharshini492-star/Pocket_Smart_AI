from pathlib import Path
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import init_db
from app.routes.auth import router as auth_router
from app.routes.planners import router as planner_router
from app.routes.session import router as session_router


BASE_DIR = Path(__file__).resolve().parent.parent

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="PocketSmart AI",
    description="Smart Budget & Recommendation Assistant",
    version="1.0.0",
    lifespan=lifespan
)


app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static"
)


app.include_router(auth_router)
app.include_router(planner_router)
app.include_router(session_router)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )


@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse(
        "register.html",
        {"request": request}
    )


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request}
    )


@app.get("/home-planner", response_class=HTMLResponse)
async def home_planner(request: Request):
    return templates.TemplateResponse(
        "home_planner.html",
        {"request": request}
    )


@app.get("/party-planner", response_class=HTMLResponse)
async def party_planner(request: Request):
    return templates.TemplateResponse(
        "party_planner.html",
        {"request": request}
    )


@app.get("/jewelry-planner", response_class=HTMLResponse)
async def jewelry_planner(request: Request):
    return templates.TemplateResponse(
        "jewelry_planner.html",
        {"request": request}
    )


@app.get("/history", response_class=HTMLResponse)
async def history_page(request: Request):
    return templates.TemplateResponse(
        "history.html",
        {"request": request}
    )


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "PocketSmart AI"
    }