import os

import requests


WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY,
    }

    response = requests.get(WEATHER_API_URL, params=params)
    response.raise_for_status()

    data = response.json()

    print(f"City: {data['location']['name']}")
    print(f"Country: {data['location']['country']}")
    print(f"Temperature: {data['current']['temp_c']}°C")
    print(f"Condition: {data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
