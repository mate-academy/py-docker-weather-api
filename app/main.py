import os

import requests

api_key = os.environ.get("API_KEY")
URL = " http://api.weatherapi.com/v1/forecast.json?"
FILTERING = "Paris"


def get_weather() -> None:
    params = {
        "key": api_key,
        "q": FILTERING
    }
    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        weather_data = response.json()

        location_info = weather_data["location"]

        city = location_info["name"]
        country = location_info["country"]
        localtime = location_info["localtime"]

        weather_current = weather_data["current"]

        temp_c = weather_current["temp_c"]
        condition = weather_current["condition"]["text"]

        print(f"Performing request to Weather API for city {city}..")
        print(f"{city}/{country} {localtime} "
              f"Weather: {temp_c} Celsius, {condition}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_weather()
