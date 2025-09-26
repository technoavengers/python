import os
from fastapi import FastAPI
import httpx
import uvicorn
from dotenv import load_dotenv
import asyncio

load_dotenv()


async def get_weather(city: str):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    if "weather" in data and "main" in data:
        return {
            "location": city.title(),
            "temperature": data['main']['temp'],
            "unit": "Celsius",
            "description": data['weather'][0]['description']
        }
    else:
        return {"error": f"Could not fetch weather for {city}."}

async def get_weather_for_cities():
    await asyncio.gather(
        get_weather("London"),
        get_weather("New York"),
        get_weather("Tokyo"),
        get_weather("Delhi")
    )

if __name__ == "__main__":
    print(asyncio.run(get_weather("London")))
    print(asyncio.run(get_weather("New York")))
    print(asyncio.run(get_weather("Tokyo")))
    print(asyncio.run(get_weather("Delhi")))

    asyncio.run(get_weather_for_cities())