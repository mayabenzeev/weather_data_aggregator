import os
import json

from app.geocoding import fetch_coordinates
from app.weather import fetch_weather
from app.analyzer import Analyzer

def analyze_weather(city: str) -> str:
    """
    Analyze the weather of a city
    Args:
        city: str
    Returns:
        str
    """
    weather_data = fetch_city_json(city, return_json=True)
    analyzer = Analyzer(weather_data, city)
    return analyzer.generate_analysis()
    
def get_weather_info(city: str) -> str:
    """
    Get the weather info of a city
    Args:
        city: str
    Returns:
        str
    """
    weather_data = fetch_city_json(city, return_json=True)
    analyzer = Analyzer(weather_data, city)
    return analyzer.generate_info_report()


def fetch_city_json(city: str, return_json: bool = False) -> dict:
    """
    Get the city json from the local folder
    Args:
        city: str
    Returns:
        dict"""
    os.makedirs("data", exist_ok=True)
    
    if not __is_city_exists(city):
        lon, lat = fetch_coordinates(city)
        weather_data = fetch_weather(lon, lat)
        with open(f"app/data/{city}.json", "w") as f:
            json.dump(weather_data, f)
    else:
        with open(f"app/data/{city}.json", "r") as f:
            weather_data = json.load(f)

    if return_json:
        return weather_data
    

def __is_city_exists(city: str) -> bool:
    """Checks if the city is in the local folder of jsons (data fetched from open-meteo)"""
    return os.path.exists(f"app/data/{city}.json")

