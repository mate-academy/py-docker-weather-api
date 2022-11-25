import os

import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json?key="
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY}...")

    url = BASE_URL + API_KEY + "&q=" + CITY
    result = requests.get(url)

    if result.status_code == 200:
        response = result.json()

        for key, values in response.items():
            print(f"{str(key).upper()}:")

            for value_key, value in values.items():
                print(f"    {value_key}: {value}")

    else:
        print("Can't access HTTP request")


if __name__ == "__main__":
    get_weather()
