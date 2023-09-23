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

    if response.status_code == 200:
        data = response.json()

        city = data["location"]["name"]
        country = data["location"]["country"]
        localtime = data["location"]["localtime"]
        temp_c = data["current"]["temp_c"]
        description = data["current"]["condition"]["text"]

        print(f"Performing request to Weather API for city {city}..")
        print(f"{city}/{country} {localtime} "
              f"Weather: {temp_c} Celsius, {description}")

    else:
        print(response.status_code)


if __name__ == "__main__":
    get_weather()
