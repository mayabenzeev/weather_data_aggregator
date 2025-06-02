from fastapi.testclient import TestClient
from app.api import app
import pytest

client = TestClient(app)

def test_fetch_cities():
    """Test fetching weather data for multiple cities"""
    response = client.post(
        "/fetch",
        json={"cities": ["London", "Berlin"]}
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert all(city["status"] == "success" for city in data)

def test_get_analytics():
    """Test getting analytics for a city"""
    # First fetch data for the city
    client.post("/fetch", json={"cities": ["London"]})
    
    # Then get analytics
    response = client.get("/analytics/London")
    assert response.status_code == 200
    data = response.json()
    assert "lowest_avg_temp" in data
    assert "highest_avg_temp" in data

def test_get_data():
    """Test getting raw weather data for a city"""
    # First fetch data for the city
    client.post("/fetch", json={"cities": ["London"]})
    
    # Then get the raw data
    response = client.get("/data/London")
    assert response.status_code == 200
    data = response.json()
    assert "daily" in data

def test_fetch_invalid_city():
    """Test error handling for invalid city names"""
    response = client.post(
        "/fetch",
        json={"cities": ["InvalidCityName123"]}
    )
    assert response.status_code == 200
    data = response.json()
    assert data[0]["status"] == "error"

def test_get_nonexistent_city_data():
    """Test error handling for getting data of non-existent city"""
    response = client.get("/data/NonExistentCity")
    assert response.status_code == 400

def test_empty_cities_list():
    """Test error handling for empty cities list"""
    response = client.post(
        "/fetch",
        json={"cities": []}
    )
    assert response.status_code == 200
    assert len(response.json()) == 0 