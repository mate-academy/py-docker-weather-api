import os
import requests

URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"
PARAMS = {"key": API_KEY, "q": CITY}


def get_weather() -> None:
    response = requests.get(URL, params=PARAMS).json()
    city = response["location"]["name"]
    country = response["location"]["country"]
    date = response["location"]["localtime"]
    temperature = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]
    print(f"Performing request to Weather API for city {city}...")
    print(f"{city}/{country} {date} "
          f"Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
