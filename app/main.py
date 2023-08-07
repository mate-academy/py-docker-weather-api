import os
import requests


API_KEY = os.environ.get("Weather_KEY")
CITY = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    parameters = {
        "key": API_KEY,
        "q": CITY,
    }
    print(f"Performing request to Weather API for city {CITY}...")
    result = requests.get(URL, params=parameters)
    data = result.json()

    city = data["location"]["name"]
    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{city}/{country} {localtime}"
          f" Weather: {temp_c} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
