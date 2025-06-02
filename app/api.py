from fastapi import FastAPI, HTTPException
from app.fetcher import fetch_and_store
from app.analytics import get_analytics, load_raw_data

app = FastAPI()

@app.post("/fetch")
def fetch_weather(payload: dict):
    cities = payload.get("cities", [])
    fetch_and_store(cities)
    return {"status": "success", "cities": cities}

@app.get("/analytics/{city}")
def analytics(city: str):
    return get_analytics(city)

@app.get("/data/{city}")
def get_data(city: str):
    return load_raw_data(city)
