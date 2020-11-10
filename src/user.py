from .db import session
from .model.user import UserTable, CreateUser
from fastapi import HTTPException
import bcrypt

def fetch_user_info(user_id: str):
  user = session.query(UserTable).filter(UserTable.id == user_id).first()
  return user

def search_user(userID: str):
  return session.query(UserTable).filter(UserTable.id == userID).first()

def create_user(userID: str, name: str, pass_hash: str, email: str):
  user = UserTable()
  if search_user(userID):
    raise HTTPException(status_code=409, detail="UserID is already registered")
  user.id = userID
  user.name = name
  user.password_hash = pass_hash
  user.email = email
  session.add(user)
  session.commit()
  return {"successed registering user!"}
