# Paris Weather Docker Service

This service fetches the current weather in Paris using WeatherAPI and Docker.

## Docker Pull Command

COMMAND=docker pull serhiibudko/paris-weather

## 🚀 Run the Container

Make sure to pass your WeatherAPI key using environment variable `API_KEY`.

```bash
docker run -e API_KEY=your_real_api_key serhiibudko/paris-weather