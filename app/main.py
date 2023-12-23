import requests
from datetime import datetime
import os


def get_weather() -> None:
    BASE_URL = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": os.environ.get("API_KEY"),
        "q": "Paris",
    }

    current_datetime = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        weather_data = response.json()

        location = weather_data["location"]["name"]
        temperature_celsius = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]

        print(f"Weather in {location} at {current_datetime}:")
        print(f"Temperature: {temperature_celsius}°C")
        print(f"Condition: {condition}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
