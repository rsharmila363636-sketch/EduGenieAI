from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from schemas import InputText
from qna import get_answer
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_path

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home(request: Request):
     return templates.TemplateResponse("index.html", {"request": request})
    

@app.post("/qa")
def qa(data: InputText):
    return {"result": get_answer(data.text)}


@app.post("/explain")
def explain(data: InputText):
    return {"result": explain_concept(data.text)}
