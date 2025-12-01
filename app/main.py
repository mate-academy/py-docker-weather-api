import requests
import os


WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"  # noqa:  N806
CITY = "Paris"  # noqa:  N806


def get_weather() -> None:
    weather = {
        "q": CITY,
        "key": os.getenv("API")
    }
    response = requests.get(WEATHER_API_URL, params=weather)
    print(response.json())


if __name__ == "__main__":
    get_weather()
