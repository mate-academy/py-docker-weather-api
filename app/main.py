import os
import requests

from dotenv import load_dotenv
load_dotenv(".env")

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    payload = {"key": API_KEY, "q": CITY}
    result = requests.get(URL, params=payload)
    if result.status_code == 200:
        weather_data = result.json()
        location = weather_data["location"]
        weather = weather_data["current"]
        print(
            f"{location['name']}/{location['country']} "
            f"{location['localtime']} Weather: {weather['temp_c']} Celsius, "
            f"{weather['condition']['text']}"
        )
    else:
        print(f"Invalid request: {result.status_code}")


if __name__ == "__main__":
    get_weather()
