from fastapi import FastAPI
from pymongo import AsyncMongoClient
app = FastAPI()
client = AsyncMongoClient("mongodb://localhost:27017")
db = client["college"]
#select collection
students_collection = db["student"]
@app.get("/")
async def home():
    return {"message": "Welcome to the FastAPI MongoDB example!"}

@app.get("/health")
async def health():
    result = await db.command("ping")
    return {"mongodb":"connected","ping":result["ok"]}
