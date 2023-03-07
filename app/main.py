import os

import requests
from dotenv import load_dotenv


load_dotenv()

api_key = os.environ.get("API_KEY")
WEATHER_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    response = requests.get(
        WEATHER_URL,
        params=[("key", api_key), ("q", "Paris")]
    )
    if response.status_code == 200:
        data = response.json()
        current_weather = data["current"]
        temperature = current_weather.get("temp_c")
        humidity = current_weather.get("humidity")
        pressure = current_weather.get("pressure_mb")
        cloud = current_weather.get("cloud")
        last_updated = current_weather.get("last_updated").split(" ")
        print("Weather in Paris")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} mbar")
        print(f"Cloud cover: {cloud}%")
        print(f"Last updated {last_updated[0]} at {last_updated[1]}")
    else:
        print("Error in the HTTP request")


if __name__ == "__main__":
    get_weather()
