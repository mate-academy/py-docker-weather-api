import os
import requests

API_KEY = os.environ.get("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY environment variable is not set")

BASE_URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    response = requests.get(BASE_URL, params={"key": API_KEY, "q": FILTERING})
    response.raise_for_status()
    data = response.json()
    weather_report = (
        f'{data["location"]["name"]}/{data["location"]["country"]} '
        f'{data["location"]["localtime"]} '
        f'Weather: {data["current"]["temp_c"]} '
        f'Celsius, {data["current"]["condition"]["text"]}'
    )
    print(weather_report)


if __name__ == "__main__":
    get_weather()
