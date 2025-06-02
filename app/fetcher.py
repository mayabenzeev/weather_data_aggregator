import requests
import json

def fetch_cities_longlat(city: str) -> tuple[float, float]:
    """
    Fetch the longitude and latitude of a city
    Args:
        city: str
    Returns:
        tuple[float, float]
    """
    url_longlat = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(url_longlat, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch longitude and latitude for city {city}")
    
    response_json = response.json()
    country = response_json['results'][0]['country']
    long, lat = response_json['results'][0]['longitude'], response.json()['results'][0]['latitude']
   
    print(f"Found long lat of {city} in country: {country}")
    return long, lat

def fetch_cities_weather(long: float, lat: float) -> dict:
    """
    Fetch the weather of a city
    Args:
        long: float
        lat: float
    Returns:
        dict
    """
    url_weather = f"https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": long,
        "forecast_days": 7,
        "daily": ["temperature_2m_max", "temperature_2m_min", "daylight_duration", "rain_sum"]
    }
    response = requests.get(url_weather, params=params)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch weather for coordinates {long}, {lat}")
    return response.json()

print(fetch_cities_weather(*fetch_cities_longlat("London")))
# print((fetch_cities_longlat("")))