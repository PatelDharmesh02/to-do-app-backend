from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal, engine
from models import Todos

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Todos.metadata.create_all(bind=engine)

class TodoResponse(BaseModel):
    id: int
    description: str
    completed: bool
    
    
class TodoAdd(BaseModel):
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
@app.post("/add_todo", response_model=TodoResponse)
def add_todo(todo: TodoAdd, db: Session = Depends(get_db)):
    db_todo = Todos(
        description=todo.description,
        completed=todo.completed
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.delete("/delete_todo/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(Todos).filter(Todos.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"status_code": 200, "detail": "Task deleted successfully!"}
    