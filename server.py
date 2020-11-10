from fastapi import FastAPI, Depends, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel
from src import auth, user
from src.model.user import UserTable, LoginUser, CreateUser, userInfo
from src.model.auth import authType

app = FastAPI()
security = HTTPBearer()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/login")
async def login(user: LoginUser) -> authType:
  return auth.authenticate(user.id, user.password)

@app.post("/register")
async def register_user(creUser: CreateUser) -> str:
  return user.create_user(
    auth.check_res_data(creUser.id),
    auth.check_res_data(creUser.name), 
    auth.hash_password(creUser.password), 
    auth.check_res_data(creUser.email)
  )

@app.get("/my")
async def read_current_user(cred: HTTPAuthorizationCredentials = Security(security)) -> userInfo:  
  return auth.get_current_user_from_token(cred.credentials)
