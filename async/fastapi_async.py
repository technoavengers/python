from myweatherapp import FastAPI
import asyncio

app = FastAPI()

@app.get("/hello")
async def say_hello():
    await asyncio.sleep(2)   # pretend slow work (like API call / DB query)
    return {"message": "Hello, world!"}