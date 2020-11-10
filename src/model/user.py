from sqlalchemy import Column, String
from pydantic import BaseModel
from ..db import Base, engine

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


def main():
  Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
  main()