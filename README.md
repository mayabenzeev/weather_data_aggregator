## *Weather Data Aggregator*


A tool that fetches, processes, and analyzes historical weather data for different cities.  

## Features

- Accepts a list of city names
- Fetches weather data (past 7 days) from a public API (e.g., [Open-Meteo](https://open-meteo.com/))
- Stores and processes the data
- Generates simple analytics (e.g., hottest/coldest day, average temperature)
- Allows retrieval via API and CLI

**Tools used:** Python (`FastAPI`, `argsparse`, `pytest`) pip, and Docker.

---

### Features & Running instructions

**1. CLI Tool**  
 Fetch
  - Fetches and stores last 7 days’ weather data for listed cities.
  - Saves data as `app/data/{city}.json`

##### Run via Python terminal (need for python, pip and requirements.txt instllation):  
  ```sh
  python app/main.py fetch --cities London Berlin Paris
  ```
##### Run via Docker:
```sh
docker build -t weather .
```
  ```sh
  docker run --rm -v $PWD/app/data:/app/data weather fetch --cities London Berlin Paris
  ```
Analyze
  - Returns hottest/coldest days, average temperature, rain sum, and daylight duration.

##### Run via Python terminal (need for python, pip and requirements.txt instllation):  
  ```sh
  python app/main.py analyze --city Tel\ Aviv
  ```
##### Run via Docker:
```sh
docker build -t weather .
```
  ```sh
  docker run --rm -v $PWD/app/data:/app/data weather analyze --city Tel\ Aviv
  ```

**2. REST API**  
#### Run the container for RestAPI
```sh
docker build -t weather .
```
```sh
 docker run -p 8000:8000 weather-app uvicorn app.api:app --host 0.0.0.0 --port 8000 
 ```

#### Endpoints:

- `POST /fetch`  
  - Payload: `{ "cities": ["London", "Berlin"] }`
  - Fetches and stores weather data for given cities.

- `GET /analytics/{city}`  
  - Returns analytics: - hottest/coldest days, average temperature, rain sum, and daylight duration.

- `GET /data/{city}`  
  - Returns raw weather data (as JSON).

---