FROM python:3.8-alpine

WORKDIR /app

COPY . .

RUN apk add --no-cache --update gcc musl-dev python3-dev libffi-dev openssl-dev build-base mariadb-connector-c-dev
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port", "3000"]
