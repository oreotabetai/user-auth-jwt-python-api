from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/login")
def login_user():
    return {"return jwt if authorize"}

@app.post("/register")
def register_user():
    return {"register user"}

@app.get("/users/{user_id}")
def get_info(user_id: int):
    return {"return user " + str(user_id) + "information"}
