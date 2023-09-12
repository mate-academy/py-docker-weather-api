import os

import requests


API_KEY = os.environ.get("API_KEY")
URL = " http://api.weatherapi.com/v1/forecast.json?"
FILTERING = "Paris"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": FILTERING
    }
    response = requests.get(URL, params=params)

    try:
        response.raise_for_status()
        data = response.json()

        city = data["location"]["name"]
        country = data["location"]["country"]
        localtime = data["location"]["localtime"]
        temp_c = data["current"]["temp_c"]
        description = data["current"]["condition"]["text"]

        print(f"Performing request to Weather API for city {city}..")
        print(f"{city}/{country} {localtime} "
              f"Weather: {temp_c} Celsius, {description}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch weather data. An error occurred: {e}")


if __name__ == "__main__":
    get_weather()
