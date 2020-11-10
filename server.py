from fastapi import FastAPI, Depends, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel
from src import auth, user
from src.model.user import UserTable

class User(BaseModel):
  name: str
  password: str

app = FastAPI()
security = HTTPBearer()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/login")
async def login(user: User):
  return auth.authenticate(user.name, user.password)

@app.post("/register")
async def register_user():
  return user.create_user()

@app.get("/my")
async def read_current_user(cred: HTTPAuthorizationCredentials = Security(security)):  
  return auth.get_current_user_from_token(cred.credentials)
