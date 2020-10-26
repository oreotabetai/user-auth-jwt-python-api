FROM python:3.8

WORKDIR /app

COPY . .

RUN  pip install pipenv

#RUN pipenv install --python 3.8.0

RUN pipenv install fastapi jwt