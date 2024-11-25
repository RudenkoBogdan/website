from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.testclient import TestClient
import os

app = FastAPI()

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

static_path = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")

@app.get("/", response_class=HTMLResponse)
async def resume(request: Request):
    data = {
        "name": "Bogdan Alenovich Rudenko",
        "profession": "Data Science, Machine Learning",
        "bio": "AI enthusiast, theoretical physicist, astronomer",
        "skills": [
            "Python for data analysis",
            "NumPy, Pandas", 
            "ML and DL",
            "Sklearn, Pytorch", 
            "Data Visualisation",
            "Matplotlib, Seaborn, Plotly, Bokeh", 
            "Math",
            "Calculus, linear algebra, probability theory, mathematical statistics" 
        ],
        "contact": {
            "email": "rudenko.ba03@gmail.com",
            "phone": "+7 925 240 27 36",
            "linkedin": "https://www.linkedin.com/in/bogdan-rudenko-3bb926323/",
            "kaggle": "https://www.kaggle.com/rudenkobogdan",
            "github": "https://github.com/RudenkoBogdan"
        },
    }
    return templates.TemplateResponse("resume.html", {"request": request, "data": data})
