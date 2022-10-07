import os
import requests

WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "Paris"


def get_weather() -> None:
    res = requests.get(WEATHER_API_URL, {
        "key" : API_KEY,
        "q": CITY,
    }).json()
    print(f"Current temperature in {CITY} is {res['current']['temp_c']} "
          f"degrees by Celsius.")


if __name__ == "__main__":
    get_weather()
