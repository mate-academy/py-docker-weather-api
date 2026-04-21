import os

import requests

API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    response = requests.get(
        API_URL,
        params={"key": api_key, "q": CITY},
        timeout=10,
    )
    response.raise_for_status()

    weather_data = response.json()["current"]
    condition = weather_data["condition"]["text"]
    temperature = weather_data["temp_c"]
    feels_like = weather_data["feelslike_c"]
    humidity = weather_data["humidity"]

    print(
        f"Current weather in {CITY}: "
        f"{condition}, {temperature}C,"
        f" feels like {feels_like}C, humidity {humidity}%"
    )


if __name__ == "__main__":
    get_weather()
