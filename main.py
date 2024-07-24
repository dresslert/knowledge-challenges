from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
import uvicorn

# Importar os esquemas e serviços
from schemas import ChallengeCreate, UserCreate, FeedbackCreate
from services import create_challenge, get_challenges, create_user, get_users, create_feedback, get_feedbacks

# Criação da aplicação FastAPI
app = FastAPI()

# Configuração do Jinja2
templates = Jinja2Templates(directory="templates")

# Configuração para servir arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Dependência para obter uma sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Roteamento para a tela inicial
@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Roteamento para Desafios
@app.post("/challenges/", response_model=ChallengeCreate)
def add_challenge(challenge: ChallengeCreate, db: Session = Depends(get_db)):
    return create_challenge(db=db, challenge=challenge)

@app.get("/challenges/")
def read_challenges(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_challenges(db=db, skip=skip, limit=limit)

# Roteamento para Usuários
@app.post("/users/", response_model=UserCreate)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@app.get("/users/")
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_users(db=db, skip=skip, limit=limit)

# Roteamento para Feedback
@app.post("/feedbacks/", response_model=FeedbackCreate)
def add_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    return create_feedback(db=db, feedback=feedback)

@app.get("/feedbacks/")
def read_feedbacks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_feedbacks(db=db, skip=skip, limit=limit)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
