from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from babel import babel
from fastapi.staticfiles import StaticFiles
import uvicorn


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')


class APIResponse(BaseModel):
    page_number: str
    page: str


class APIPageLookupRequest(BaseModel):
    page_number: str


@app.get("/api/random", response_model=APIResponse)
async def get_random_page(request: Request):
    seed = babel.random_page_number()
    page = babel.generate_page(seed)

    response = APIResponse(
        page_number=str(seed),
        page=page,
    )

    return response


@app.post("/api/page", response_model=APIResponse)
async def get_page_by_number(page: APIPageLookupRequest, request: Request):
    page_number = page.page_number
    try:
        seed_int = int(page_number)
        if seed_int > babel.TOTAL_PAGES - 1:
            raise ValueError(f"Maximum page number is {babel.TOTAL_PAGES - 1}")
        if seed_int < 0:
            raise ValueError("Minimum page number is 0")
    except ValueError:
        raise HTTPException(
            status_code=400, detail="Page number must be integer in the following range: [0; (27**1024) - 1]")

    page = babel.generate_page(seed_int)

    response = APIResponse(
        page_number=page_number,
        page=page,
    )
    return response


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/page", response_class=HTMLResponse)
async def get_page(request: Request):
    return templates.TemplateResponse(request=request, name="form.html")


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(request=request, name="about.html")

if __name__ == "__main__":
    config = uvicorn.Config("main:app", host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
