from sqlalchemy import Boolean, Column, Integer, String
from database import Base
from pydantic import BaseModel


class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(225))
    completed = Column(Boolean, default=False)


class TodoResponse(BaseModel):
    id: int
    description: str
    completed: bool
    
    
class TodoAdd(BaseModel):
    description: str
    completed: bool
    
class TodoEditDescription(BaseModel):
    description: str
    
class TodoEditStatus(BaseModel):
    completed: bool