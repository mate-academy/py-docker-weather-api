import os

import requests


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")

    api_key = os.getenv("API_KEY")

    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": api_key,
        "q": "Paris",
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    city = data["location"]["name"]
    country = data["location"]["country"]
    date_time = data["current"]["last_updated"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(
        f"{city}/{country} {date_time}"
        f"Weather: {temperature : .1f} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
