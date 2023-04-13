import requests
import os

WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    payload = {"key": API_KEY, "q": "SW1"}

    response = requests.get(WEATHER_API_URL, payload)

    print(response.content)


if __name__ == "__main__":
    get_weather()
