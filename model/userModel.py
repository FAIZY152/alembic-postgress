from sqlalchemy import Column, Integer, String, DateTime,Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# model for todos
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String)
    status = Column(Boolean, default=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)   