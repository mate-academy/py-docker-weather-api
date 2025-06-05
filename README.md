# Weather App Docker Project

This project implements a simple service to get current weather for Paris using WeatherAPI,
dockerized and pushed to Docker Hub.

## How to run

To pull and run the Docker image, use the following commands.
Replace `YOUR_API_KEY` with your actual WeatherAPI key.

```bash
docker pull batyarandrii/weather-app:latest
docker run --rm -e API_KEY="YOUR_API_KEY" batyarandrii/weather-app:latest