from fastapi import FastAPI
from typing import List
from starlette.middleware.cors import CORSMiddleware
from db import session
from model import UserTable, User
import pymysql
pymysql.install_as_MySQLdb()

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


#@app.get("/users")                      #사용자를 읽음
def read_users():
    users=session.query(UserTable).all()
    return read_users

#@app.get("/users/{user_id}")
#def read_users(user_id:int):
#    user=session.query(UserTable).filter(UserTable==user_id).first()
#    return read_users

@app.post("/user_create")
def create_users(id: str, password:str):
    user=UserTable()
    user.id=id
    user.pwd=password

    session.add(user)
    session.commit()
    return f"{id} created..."

@app.put("/user_update")
def update_users(user: List[User]):
    for i in user:
        user=session.query(UserTable).filter(UserTable.id_n==i.id_n).first()
        user.id=i.id
        user.pwd=i.pwd
        session.commit()

    return f"{i.id} updated..."

@app.delete("/user_delete")
def delete_users(user_id_number:int):
    user=session.query(UserTable).filter(UserTable.id_n==user_id_number).delete()
    session.commit()
    return read_users
