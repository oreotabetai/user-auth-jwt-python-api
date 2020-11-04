from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException
from datetime import datetime, timedelta
import jwt

fake_users_db = {
  "yamakenji": {
      "id": "base64id",
      "username": "yamakenji",
      "full_name": "Kenji Yamashita",
      "email": "sample@example.com",
      "password": "fakehashedsecret",
      "disabled": False,
  }
}
# for instance 
secret_key = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def create_tokens(user_id: str):
  payload = {
    'token_type': 'access_token',
    'exp': datetime.utcnow() + timedelta(minutes=2),
    'sub': user_id,
    'iss': 'change it using env later'
  }

  return jwt.encode(payload, secret_key, algorithm='HS256')

def authenticate(username: str, password: str):
  user = fake_users_db.get(username)
  if not user:
    raise HTTPException(status_code=401, detail="Incorrect username or password")

  if user["password"] != password:
    raise HTTPException(status_code=401, detail="Incorrect username or password")
  
  return {
    "access_token": create_tokens(user["id"]),
    "token_type": "bearer"
  }
  