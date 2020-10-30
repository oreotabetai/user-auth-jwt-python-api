FROM python:3.8-alpine

WORKDIR /app

COPY . .

RUN apk add --no-cache --update gcc musl-dev python3-dev libffi-dev openssl-dev
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "server.py"]