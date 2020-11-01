from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate(username: str, password: str):
  return {"return username: " + username}