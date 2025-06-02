import requests

def fetch_coordinates(city: str) -> tuple[float, float, str]:
    """
    Fetch the coordinates of a city
    Args:
        city: str
    Returns:
        tuple[float, float, str]
    """
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en"
    response = requests.get(url, headers={"Content-Type": "application/json"})
    if response.status_code != 200:
        raise Exception(f"Failed to fetch coordinates for {city}")

    data = response.json()
    if not data.get("results"):
        raise ValueError(f"No location found for '{city}'")

    result = data["results"][0]
    country = result["country"]
    print(f"Found coordinates of {city} in country: {country}")
    return result["longitude"], result["latitude"]
