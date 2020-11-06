from fastapi import FastAPI, Depends
from pydantic import BaseModel
from src import auth, user
from src.model.user import UserTable

class User(BaseModel):
  name: str
  password: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/login")
async def login(user: User):
  return auth.authenticate(user.name, user.password)

@app.post("/register")
async def register_user():
  return user.create_user()

@app.get("/users/me")
async def get_info(current_user: UserTable = Depends(auth.get_current_user)):
  return current_user
