import os

import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": api_key,
        "q": "Paris",
    }

    print("Performing request to Weather API for city Paris...")

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    print(
        f"{data['location']['name']}/{data['location']['country']} "
        f"{data['location']['localtime']} "
        f"Weather: {data['current']['temp_c']} Celsius, "
        f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
