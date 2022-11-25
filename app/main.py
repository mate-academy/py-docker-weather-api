import os
import requests


URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"
PARAMS = {"key": API_KEY, "q": CITY}


def get_weather() -> None:
    res = requests.get(URL, params=PARAMS).json()

    location = f"{res['location']['name']}/{res['location']['country']}"
    localtime = res["location"]["localtime"]
    temp_c = res["current"]["temp_c"]
    condition = res["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {CITY}...")
    print(f"{location} {localtime} Weather: {temp_c} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
