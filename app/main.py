import os
import requests

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    res = requests.get(URL, {
        "key": API_KEY,
        "q": CITY
    }).json()

    city = res["location"]["name"]
    country = res["location"]["country"]
    localtime = res["location"]["localtime"]
    weather = res["current"]["temp_c"]
    condition = res["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {city}...")
    print(f"{city}/{country} {localtime} "
          f"Weather: {weather} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
