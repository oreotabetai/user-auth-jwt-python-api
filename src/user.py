import sys
sys.path.append('../')
from db import session
from model.user import UserTable

def fetch_user_info(user_id: str):
  user = session.query(UserTable).filter(UserTable.id == user_id).first()
  return user

def search_user(username: str):
  return session.query(UserTable).filter(UserTable.name == username).first()

def create_user():
  return {"register user"}
