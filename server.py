from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from auth import authenticate
from user import fetch_user_info, create_user

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
  return authenticate(form.username, form.password)

@app.post("/register")
async def register_user():
  return create_user()

@app.get("/users/{user_id}")
async def get_info(user_id: str):
  return fetch_user_info(user_id)
