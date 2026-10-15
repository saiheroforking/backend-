
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "FastAPI backend is running!"}

@app.get("/api/users")
def get_users():
    return [
        {"id": 1, "name": "Sai"},
        {"id": 2, "name": "Rahul"},
        {"id": 3, "name": "Priya"},
    ]


@app.get("/api/users/sai")
def get_user_sai():
    return [
        {"id":1,"name":"sai"}
    ]
