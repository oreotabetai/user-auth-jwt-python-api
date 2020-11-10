from fastapi import HTTPException
from datetime import datetime, timedelta
from .user import fetch_user_info, search_user
import os, jwt, bcrypt

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

def authenticate(userID: str, password: str):
  user = search_user(userID)
  if not user:
    raise HTTPException(status_code=401, detail="Incorrect username or password")
  if not bcrypt.checkpw(password.encode(), user.password_hash.encode()):
    raise HTTPException(status_code=401, detail="Incorrect username or password")
  
  return {
    "access_token": create_tokens(user.id),
    "token_type": "bearer"
  }

def get_current_user_from_token(token: str):
  try:
    payload = jwt.decode(token, public_key, algorithms='RS256')
  except:
    raise HTTPException(status_code=401, detail="Invalid token")

  if payload['token_type'] != 'access_token':
    raise HTTPException(status_code=401, detail="Invalid Token Type")

  user = fetch_user_info(payload['sub'])
  return {
    'id': user.id,
    'name': user.name,
    'email': user.email,
  }

def hash_password(password: str):
  chkpass = check_res_data(password)
  return bcrypt.hashpw(chkpass.encode(), bcrypt.gensalt())

def check_res_data(res_data: str):
  if len(res_data) <= 0:
    raise HTTPException(status_code=400, detail="Wrong format for creating user")
  return res_data
