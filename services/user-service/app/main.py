from fastapi import FastApi

app = FastAPI()

@app.get("/")
async def root():
    return {"service": "user-service", "status": "running"}

@app.get("/users")
async def get_users():
    return [
        {"id": 1, "username": "ana"},
        {"id": 2, "username": "ivan"}
    ]