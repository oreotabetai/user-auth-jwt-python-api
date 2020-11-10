from sqlalchemy import Column, String
from pydantic import BaseModel
from ..db import Base, engine

userInfo = {
  "id": str,
  "name": str,
  "email": str,
}

# userテーブルのモデル
class UserTable(Base):
  __tablename__ = "users"
  id = Column(String, primary_key=True)
  name = Column(String)
  password_hash = Column(String)
  email = Column(String)

class User(BaseModel):
  id: str
  name: str
  password_hash: str
  email: str

class LoginUser(BaseModel):
  id: str
  password: str

class CreateUser(BaseModel):
  id: str
  name: str
  password: str
  email: str

def main():
  Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
  main()