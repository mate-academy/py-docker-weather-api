import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise RuntimeError("API_KEY is not set")

    print("Performing request to Weather API for city Paris...")

    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": "Paris"
    }

    response = requests.get(url, params=params)
    data = response.json()

    location = data["location"]["name"]
    country = data["location"]["country"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{location}/{country} {temp} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
