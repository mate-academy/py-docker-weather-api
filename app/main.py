import os
import requests

WEATHER_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")
    params = {"key": api_key, "q": CITY}
    response = requests.get(WEATHER_URL , params=params)
    data = response.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    time = data["location"]["localtime"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    print(
        f"Performing request to Weather API for city {CITY}...\n"
        f"{city}/{country} {time} "
        f"Weather: {temp} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
