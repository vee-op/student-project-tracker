from fastapi import FastAPI
from app.routes import register, status, update

app = FastAPI(title="Cloud Native Series - Student Tracker")

app.include_router(register.router)
app.include_router(status.router)
app.include_router(update.router)

@app.get("/")
def home():
    return {"message": "Welcome to Cloud Native Series with Chisom. Use /register to join."}
