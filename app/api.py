from fastapi import FastAPI

import app.services.weather_service as weather_service

app = FastAPI(title="Weather API", description="API for weather data")

@app.post("/fetch") 
def fetch_and_save_weather(cities: list[str]):
    """
    Fetch the weather of a list of cities from open-meteo and save it to the local folder
    """
    for city in cities:
        try:
            weather_service.fetch_city_json(city)
            return {"status": "success", "message": f"Fetched weather data for {city}, saved in app/data/{city}.json"}
        except Exception as e:
            return {"status": "error", "message": f"Failed to save weather for {city}: {e}"}

@app.get("/analytics/{city}")
def analyze_weather(city: str):
    """
    Return the analytics of the weather of a city
    """
    try:
        return weather_service.analyze_weather(city)
    except Exception as e:
        return {"status": "error", "message": f"Failed to analyze weather for {city}: {e}"}

@app.get("/data/{city}")
def get_weather_data(city: str):
    """
    Return the data of a city
    """
    try:
        return weather_service.fetch_weather(city)
    except Exception as e:
        return {"status": "error", "message": f"Failed to get data for {city}: {e}"}








