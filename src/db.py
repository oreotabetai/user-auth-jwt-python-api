from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

DB_NAME = os.getenv("DB_NAME", "user-auth")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
  user_name,
  DB_PASSWORD,
  host,
  DB_NAME
)

engine = create_engine(
  DATABASE,
  encoding="utf-8",
  echo=True
)

session = scoped_session(
  sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
Base.query = session.query_property()
