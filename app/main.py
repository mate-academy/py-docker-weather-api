import os
import requests

WEATHER_API_KEY = os.getenv("API_KEY")

BASE_URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    assert WEATHER_API_KEY is not None
    result = requests.get(BASE_URL + f"key={WEATHER_API_KEY}&q={FILTERING}")
    if result.status_code == 200:
        print(result.json())
    else:
        print(f"Error: {result.status_code}, {result.text}")


if __name__ == "__main__":
    get_weather()
