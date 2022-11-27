import requests
import os


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(URL, {"key": API_KEY, "q": CITY}).json()

    city = response["location"]["name"]
    country = response["location"]["country"]
    localtime = response["location"]["localtime"]
    weather = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {city}")
    print(f"{city}/{country} {localtime} "
          f"Weather: {weather} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
