import os

import requests

API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not found in environment variables")

WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    """
    Sends a request to the WEATHER_API_URL and print the current
    weather information for the city specified by the CITY constant.
    """
    print(f"Performing request to Weather API for city {CITY}...")

    try:
        params = {"key": API_KEY, "q": CITY}
        response = requests.get(WEATHER_API_URL, params=params).json()

        country = response["location"]["country"]
        _datetime = response["location"]["localtime"]
        temperature = response["current"]["temp_c"]
        condition = response["current"]["condition"]["text"]

        print(
            f"{country}/{CITY} {_datetime} "
            f"Weather: {temperature} Celsius, {condition}"
        )

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")

    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")


if __name__ == "__main__":
    get_weather()
