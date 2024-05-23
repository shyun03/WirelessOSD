from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from db import Base
from db import ENGINE

class UserTable(Base):
    __tablename__ = 'OSD_table'
    id_n =Column(Integer, primary_key=True, autoincrement=True)
    id = Column(String(58), nullable=False)
    pwd=Column(String(58), nullable=False)

class User(BaseModel):
    id_n:int
    id:str
    pwd:str
