import os
import sys
import requests


WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API_KEY environment variable is not set")
        sys.exit(1)

    params = {
        "key": api_key,
        "q": CITY,
        "aqi": "no",
    }

    response = requests.get(WEATHER_API_URL, params=params)
    response.raise_for_status()

    data = response.json()

    location = data["location"]["name"]
    country = data["location"]["country"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    wind_kph = data["current"]["wind_kph"]
    humidity = data["current"]["humidity"]

    print(f"City: {location}, {country}")
    print(f"Temperature: {temp_c}°C")
    print(f"Condition: {condition}")
    print(f"Wind: {wind_kph} kph")
    print(f"Humidity: {humidity}%")


if __name__ == "__main__":
    get_weather()
