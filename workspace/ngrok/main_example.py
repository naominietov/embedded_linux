from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    today = datetime.now().isoformat()
    return {"message": "Hello World", "at": today}

# uvicorn main:app --reload --port 16000
# uvicorn main:app --reload --port 9600