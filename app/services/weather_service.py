import os
import json
from app.geocoding import fetch_coordinates
from app.weather import fetch_weather
from app.analysis_generator import Analyzer

def analyze_city_weather(city: str) -> str:
    """
    Analyze the weather of a city
    If the city is not in the local folder of jsons,
    it will fetch the weather data from open-meteo and save it to the local folder
    Args:
        city: str
    Returns:
        str
    """
    if not __is_city_exists(city):
        lon, lat = fetch_coordinates(city)
        weather_data = fetch_weather(lon, lat)
        with open(f"data/{city}.json", "w") as f:
            json.dump(weather_data, f)
    else:
        with open(f"data/{city}.json", "r") as f:
            weather_data = json.load(f)

    analyzer = Analyzer(weather_data, city)
    return analyzer.generate_analysis()

def __is_city_exists(city: str) -> bool:
    """Checks if the city is in the local folder of jsons (data fetched from open-meteo)"""
    return os.path.exists(f"data/{city}.json")
