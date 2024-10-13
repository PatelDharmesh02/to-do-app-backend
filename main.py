from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel

from database import SessionLocal, engine
from models import Todos

app = FastAPI()

Todos.metadata.create_all(bind=engine)

class TodoResponse(BaseModel):
    id: int
    description: str
    completed: bool
    


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/get_todos", response_model=List[TodoResponse])
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todos).all()
    return todos