# Weather API Service

A simple Python app that fetches current weather for Paris using [WeatherAPI](https://www.weatherapi.com/).  
Containerized with Docker and published on Docker Hub.

---

## Run locally
```bash
pip install -r requirements.txt
API_KEY=your_api_key python app/main.py
```

## Docker usage

Build image:
```bash
docker build -t idyriv11/weather-api .
```

Run container:
```bash
docker run --rm -e API_KEY=your_api_key idyriv11/weather-api
```

Push to Docker Hub:
```bash
docker push idyriv11/weather-api:latest
```

Pull image:
```
docker pull idyriv11/weather-api:latest
```

## Example output
```
Paris, France
Temperature: 17.1 °C
Condition: Light rain shower
Wind: 14.8 kph
Humidity: 72%
```