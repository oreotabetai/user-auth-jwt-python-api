from fastapi import FastAPI, Depends, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel
from src import auth, user
from src.model.user import UserTable, LoginUser, CreateUser


app = FastAPI()
security = HTTPBearer()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/login")
async def login(user: LoginUser):
  return auth.authenticate(user.userID, user.password)

@app.post("/register")
async def register_user(creUser: CreateUser):
  return user.create_user(
    auth.check_res_data(creUser.userID),
    auth.check_res_data(creUser.name), 
    auth.hash_password(creUser.password), 
    auth.check_res_data(creUser.email)
  )

@app.get("/my")
async def read_current_user(cred: HTTPAuthorizationCredentials = Security(security)):  
  return auth.get_current_user_from_token(cred.credentials)
