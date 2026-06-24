import os

import requests


URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    response = requests.get(
        URL,
        params={
            "key": api_key,
            "q": CITY,
            "aqi": "no",
        },
        timeout=10,
    )

    response.raise_for_status()

    weather_data = response.json()

    city = weather_data["location"]["name"]
    country = weather_data["location"]["country"]
    temperature = weather_data["current"]["temp_c"]
    condition = weather_data["current"]["condition"]["text"]
    humidity = weather_data["current"]["humidity"]
    wind_speed = weather_data["current"]["wind_kph"]

    print(f"City: {city}, {country}")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} kph")


if __name__ == "__main__":
    get_weather()
