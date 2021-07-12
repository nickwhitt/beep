from datetime import datetime
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"The time is {datetime.now()}"}
