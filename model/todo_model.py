from sqlalchemy import Column, Integer, String, DateTime,Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(Boolean, default=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)   