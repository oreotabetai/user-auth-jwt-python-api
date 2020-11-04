from fastapi import FastAPI, Depends
from pydantic import BaseModel
from auth import authenticate
from user import fetch_user_info, create_user

class User(BaseModel):
  name: str
  password: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/login")
async def login(user: User):
  return authenticate(user.name, user.password)

@app.post("/register")
async def register_user():
  return create_user()

@app.get("/users/{user_id}")
async def get_info(user_id: str):
  return fetch_user_info(user_id)
