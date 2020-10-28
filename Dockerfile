FROM python:3.8

WORKDIR /app

COPY . .

RUN  pip install pipenv

RUN pipenv install fastapi jwt