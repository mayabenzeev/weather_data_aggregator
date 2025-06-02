**Weather Data Aggregator**

## Context

A tool that fetches, processes, and analyzes historical weather data for different cities.  
The tool:
- Accepts a list of city names
- Fetches weather data (past 7 days) from a public API (e.g., [Open-Meteo](https://open-meteo.com/))
- Stores and processes the data
- Generates simple analytics (e.g., hottest/coldest day, average temperature)
- Allows retrieval via API and CLI

**Tools used:** Python, pip, and Docker.

---

### Technical Requirements

- **Python 3.8+**
- Package dependencies with **pip** (`requirements.txt`)
- **Dockerize** your application
- Cross-platform (Windows, macOS, Linux)
- Public weather API (suggested: [Open-Meteo free endpoints](https://open-meteo.com/en/docs))
- CLI implemented with `argparse` 
- REST API with **FastAPI**
- Fetched data is stored in local JSON files (one file per city)
- **Unit tests** with `pytest`

---

### Features

**1. CLI Tool**  
- Command:  
  ```sh
  python app/main.py fetch --cities London Berlin Paris
  ```
  - Fetches and stores last 7 days’ weather data for listed cities.
  - Saves data as `data/{city}.json`

- Command:  
  ```sh
  python app/main.py analyze --city London
  ```
  - Shows hottest/coldest day and average temperature for city.

**2. REST API**  
- `POST /fetch`  
  - Payload: `{ "cities": ["London", "Berlin"] }`
  - Fetches and stores weather data for given cities.

- `GET /analytics/{city}`  
  - Returns analytics: hottest/coldest day, average temp, in JSON.

- `GET /data/{city}`  
  - Returns raw weather data (as JSON).

---

### Testing Requirements

- **Unit tests** for key logic (fetching, processing, analytics)
- **Integration tests** for API endpoints (with mocking)
- Tests must run inside Docker using `pytest`

---

### Step-by-Step Implementation Guide

1. **Project Setup**  
   - Use the provided project structure
   - Install dependencies (requests, FastAPI/Flask, pytest)

2. **CLI Tool**  
   - Implement commands for fetching and analyzing data

3. **Weather Fetch Logic**  
   - Use requests to call Open-Meteo API  
   - Save responses to `data/{city}.json`

4. **Analytics Logic**  
   - Parse JSON data to find max/min/avg temperature

5. **REST API**  
   - Implement endpoints to fetch data and provide analytics

6. **Testing**  
   - Write tests for fetching, analytics, and API

7. **Dockerize**  
   - Provide Dockerfile and verify all scripts, API, and tests run in container

8. **Documentation**  
   - Add setup/run/test instructions in `README.md`

---

### Deliverables

- Full project code (CLI, API, analytics)
- `requirements.txt` and `Dockerfile`
- Tests in `/tests`
- `README.md` with clear instructions
- All code and data in one zipped directory

---

### Submission

- Zip your entire project directory and submit as  
  `yourname_weather_data_aggregator.zip`

---

### Evaluation Rubric

| Category         | Excellent (3)        | Good (2)             | Needs Work (1)    |
|------------------|---------------------|----------------------|-------------------|
| Feature Coverage | All CLI/API features, error handling, analytics | Most features, minor bugs | Major features missing/broken |
| Code Quality     | Clean, readable, modular | Some messiness | Hard to follow, poor style |
| Dockerization    | Runs perfectly in Docker | Minor issues | Fails to run/build |
| Testing          | Comprehensive and passing | Some coverage | Lacking/poor |
| Documentation    | Clear, concise, correct | Partial/unclear | Missing |
| Creativity/Bonus | Enhancements, thoughtful design | Minor extras | None |

---

## Starter Project Structure

```
weather_data_aggregator/
├── app/
│   ├── __init__.py
│   ├── main.py         # CLI entry point
│   ├── api.py          # REST API implementation
│   ├── fetcher.py      # Weather fetch & storage logic
│   └── analytics.py    # Data analysis logic
├── data/               # Saved JSON data per city
├── tests/
│   └── test_core.py    # Core logic & API tests
├── requirements.txt
├── Dockerfile
└── README.md
```
