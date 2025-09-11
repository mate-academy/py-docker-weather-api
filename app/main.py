import os
import requests


BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
TIMEOUT = 10


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY}...")
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY is not set in environment variables")

    response = requests.get(
        BASE_URL,
        params={"key": api_key, "q": CITY},
        timeout=TIMEOUT,
    )
    response.raise_for_status()

    data = response.json()
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    city = data["location"]["name"]
    country = data["location"]["country"]
    current_time = data["location"]["localtime"]

    print(
        f"{city}/{country} {current_time} Weather: {temp} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
