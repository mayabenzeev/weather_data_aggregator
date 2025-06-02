from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

import app.services.weather_service as weather_service

app = FastAPI(title="Weather API", description="API for weather data")

class Cities(BaseModel):
    cities: List[str]

@app.post("/fetch")
def fetch_and_save_weather(request: Cities):
    """
    Fetch the weather of a list of cities from open-meteo and save it to the local folder
    """
    results = []
    for city in request.cities:
        try:
            weather_service.fetch_city_json(city)
            results.append({
                "city": city,
                "status": "success",
                "message": f"Fetched weather data for {city}, saved in app/data/{city}.json"
            })
        except Exception as e:
            results.append({
                "city": city,
                "status": "error",
                "message": f"Failed to save weather for {city}: {e}"
            })
    
    return {"results": results}

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
        return weather_service.get_weather_info(city)
    except Exception as e:
        return {"status": "error", "message": f"Failed to get data for {city}: {e}"}








