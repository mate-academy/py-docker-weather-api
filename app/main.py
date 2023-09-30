import os

from requests import get
import datetime


def get_weather() -> None:
    API_KEY = os.environ.get("API_KEY")
    BASE_URL = "https://api.weatherapi.com/v1/current.json"
    params = {"key": API_KEY, "q": "Paris"}

    response = get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(
            f"Paris/France {datetime.date.today()} Weather: {temperature}°C, {condition}")
    else:
        print(f"Weather data could not be obtained")


if __name__ == "__main__":
    get_weather()
