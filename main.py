from fastapi import FastAPI
import pendulum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"The time is {pendulum.now('UTC')}"}
