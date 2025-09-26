import os
from myweatherapp import FastAPI, requests
import uvicorn
from dotenv import load_dotenv

# Create a FastAPI instance
app = FastAPI()

load_dotenv()

# Define a root endpoint
@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

@app.get("/get_weather")
async def get_weather(city: str):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
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

# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8003)

# Note: In a notebook, we'll run this differently