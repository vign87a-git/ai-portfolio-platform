import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from google import genai

app = FastAPI(title="THETRON Core Systems", version="1.0.0")
templates = Jinja2Templates(directory="app/templates")

class PromptPayload(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/favicon.svg")
async def get_favicon():
    return FileResponse("app/templates/favicon.svg", media_type="image/svg+xml")

@app.get("/architecture", response_class=HTMLResponse)
@app.get("/architecture.html", response_class=HTMLResponse)
async def get_architecture(request: Request):
    return templates.TemplateResponse(request=request, name="architecture.html")

@app.get("/demo", response_class=HTMLResponse)
@app.get("/demo.html", response_class=HTMLResponse)
async def get_demo(request: Request):
    return templates.TemplateResponse(request=request, name="demo.html")

@app.get("/projects", response_class=HTMLResponse)
@app.get("/projects.html", response_class=HTMLResponse)
async def get_projects(request: Request):
    return templates.TemplateResponse(request=request, name="projects.html")

@app.get("/rag", response_class=HTMLResponse)
@app.get("/rag.html", response_class=HTMLResponse)
async def get_rag(request: Request):
    return templates.TemplateResponse(request=request, name="rag.html")

@app.get("/telemetry", response_class=HTMLResponse)
@app.get("/telemetry.html", response_class=HTMLResponse)
async def get_telemetry(request: Request):
    return templates.TemplateResponse(request=request, name="telemetry.html")

@app.post("/generate")
async def generate_content(payload: PromptPayload):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return {"error": "GEMINI_API_KEY environment variable is not configured."}
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=payload.text,
        )
        return {"reply": response.text}
    except Exception as e:
        return {"error": str(e)}
