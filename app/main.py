import os
import requests


REQUEST_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY
    }
    response = requests.get(REQUEST_URL, params=params).json()

    city = response["location"]["name"]
    country = response["location"]["country"]
    date = response["location"]["localtime"]
    temperature = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]

    print(f"Performing request to weather API for city: {city}...")
    print(f"{city}/{country} {date} Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
