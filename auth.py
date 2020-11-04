from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException
from datetime import datetime, timedelta
import os 
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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

exp_duration = os.getenv("JWT_EXP_SECONDS", 120)
private_key_path = os.getenv("PRIVATE_KEY_PATH", "./key/private-key.pem")

with open(private_key_path, "rb") as key_file:
    private_key = key_file.read()
    
def create_tokens(user_id: str):
  payload = {
    'token_type': 'access_token',
    'exp': datetime.utcnow() + timedelta(seconds=exp_duration),
    'sub': user_id,
    'iss': 'change it using env later'
  }

  return jwt.encode(payload, private_key, algorithm='RS256')

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
