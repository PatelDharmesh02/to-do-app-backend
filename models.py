from sqlalchemy import Boolean, Column, Integer, String
from database import Base


class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(225))
    completed = Column(Boolean, default=False)
    