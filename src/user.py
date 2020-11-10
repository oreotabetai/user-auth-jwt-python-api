from .db import session
from .model.user import UserTable, CreateUser
from fastapi import HTTPException
import bcrypt

def fetch_user_info(user_id: str) -> UserTable:
  return session.query(UserTable).filter(UserTable.id == user_id).first()

def search_user(user_id: str) -> UserTable:
  return session.query(UserTable).filter(UserTable.id == user_id).first()

def create_user(user_id: str, name: str, pass_hash: str, email: str) -> str:
  user = UserTable()
  if search_user(user_id):
    raise HTTPException(status_code=409, detail="UserID is already registered")
  user.id = user_id
  user.name = name
  user.password_hash = pass_hash
  user.email = email
  session.add(user)
  session.commit()
  return {"successed registering user!"}
