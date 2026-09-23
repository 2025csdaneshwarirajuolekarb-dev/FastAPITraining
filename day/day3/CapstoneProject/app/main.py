#this file is the entry point the application

from fastapi import FastAPI

from app.config import settings
from app.database import ping_database
#creats FastAPI instance with title from settings
app = FastAPI(title=settings.APP_NAME)
#this function runs once when the server starts.It checks the DB connection.
@app.on_event("startup")
def on_startup() -> None:
    if not ping_database():
        raise RuntimeError("Could not connect to MongoDB")
    print(f"[startup]Connected to MongoDB. App:{settings.APP_NAME}")
# checks basic health check API endpoint and confirms 
# GET / is running and reachable
@app.get("/",tags=["Health"])
def health_check():
    return {"status": "ok", "app": settings.APP_NAME}