import os

from requests import get
import datetime


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    base_url = "https://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": "Paris"}

    response = get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(
            f"Paris/France {datetime.date.today()} "
            f"Weather: {temperature}°C, {condition}")
    else:
        print("Weather data could not be obtained")


if __name__ == "__main__":
    get_weather()
