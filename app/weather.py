import requests

def fetch_weather(longitude: float, latitude: float) -> dict:
    """
    Fetch the weather of a city
    Args:
        longitude: float
        latitude: float
    Returns:
        dict
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "forecast_days": 7,
        "daily": ["temperature_2m_max", "temperature_2m_min", "daylight_duration", "rain_sum"]
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch weather for {latitude}, {longitude}")

    return response.json()
