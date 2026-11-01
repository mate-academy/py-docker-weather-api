import os
import requests

API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("API_KEY environment variable is not set")
    params = {"key": API_KEY, "q": CITY}
    response = requests.get(URL, params=params)
    data = response.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    time = data["location"]["localtime"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    print(f"Performing request to Weather API for city {CITY}...")
    print(
        f"{city}/{country} {time} "
        f"Weather: {temp} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
