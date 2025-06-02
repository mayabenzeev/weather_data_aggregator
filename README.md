# Weather Data Aggregator

A tool that fetches, processes, and analyzes weather data for different cities.

## Quick Start

```bash
# Build the container
docker build -t weather .

# Run API server
docker run --rm -p 8000:8000 -v $PWD/app/data:/app/data --entrypoint uvicorn weather app.api:app --host 0.0.0.0 --port 8000
```

## REST API

### 1. POST /fetch
Fetches and stores weather data for given cities from open-meteo and saves it to the local folder.

Request:
```bash
curl -X POST http://localhost:8000/fetch \
  -H "Content-Type: application/json" \
  -d '{"cities": ["London", "Berlin"]}'
```

Response:
```json
{
    "results": [
        {
            "city": "London",
            "status": "success", 
            "message": "Fetched weather data for London, saved in app/data/London.json"
        },
        {
            "city": "Berlin",
            "status": "success",
            "message": "Fetched weather data for Berlin, saved in app/data/Berlin.json"
        }
    ]
}
```

### 2. GET /analytics/{city}
Returns the analytics of the weather of a city.

```bash
curl http://localhost:8000/analytics/London
```

Response:
```json
{
    "city": "London",
    "lowest_avg_temp": "12.257142857142856 °C", 
    "highest_avg_temp": "18.485714285714288 °C",
    "daylight_avg_duration": "985.93 minutes",
    "rain_avg_amount": "1.342857142857143 mm"
}
```
Includes hottest/coldest days, average temperature, and other analytics in JSON format.

### 3. GET /data/{city}
Returns the raw weather data of a city as JSON.

```bash
curl http://localhost:8000/data/London
```

## Error Handling

All endpoints return error responses in the following format:
```json
{
    "status": "error",
    "message": "Failed to get data for Jerusalm: No location found for 'Jerusalm'"
}
```

## CLI

### Local Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run locally:
Via Python terminal: 
  ```bash
  python app/main.py fetch --cities London Berlin Paris
  ```
  ```bash
  python app/main.py analyze --city Tel\ Aviv


### API Documentation

When the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Data Storage

Weather data is stored in JSON files in the `app/data/` directory. Each city's data is stored in a separate file named `{city}.json`.