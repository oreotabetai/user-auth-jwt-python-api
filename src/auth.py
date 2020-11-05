from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends
from datetime import datetime, timedelta
import os, jwt, sys
import bcrypt

from user import fetch_user_info, search_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

exp_duration = os.getenv("JWT_EXP_SECONDS", 120)
private_key_path = os.getenv("PRIVATE_KEY_PATH", "./key/private-key.pem")
public_key_path = os.getenv("PUBLIC_KEY_PATH", "./key/public-key.pem")

with open(private_key_path, "rb") as key_file:
    private_key = key_file.read()

with open(public_key_path, "rb") as key_file:
    public_key = key_file.read()

    
def create_tokens(user_id: str):
  payload = {
    'token_type': 'access_token',
    'exp': datetime.utcnow() + timedelta(seconds=exp_duration),
    'sub': user_id,
    'iss': 'change it using env later'
  }

  return jwt.encode(payload, private_key, algorithm='RS256')

def authenticate(username: str, password: str):
  user = search_user(username)
  if not user:
    raise HTTPException(status_code=401, detail="Incorrect username or password")
  
  if not bcrypt.checkpw(password, user["password"]):
    raise HTTPException(status_code=401, detail="Incorrect username or password")
  
  return {
    "access_token": create_tokens(user["id"]),
    "token_type": "bearer"
  }

def get_current_user_from_token(token: str, token_type: str):
  payload = jwt.decode(token, public_key, algorithms='RS256')

  if payload['token_type'] != token_type:
    raise HTTPException(status_code=401, detail="Invalid Token Type")
  user = fetch_user_info(payload['sub'])
  
  return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
  return get_current_user_from_token(token, 'access_token')