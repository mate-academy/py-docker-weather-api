import requests
import os
from requests.exceptions import RequestException


URL = "https://api.weatherapi.com/v1/current.json?"
API_KEY = os.getenv("API_KEY")

FILTERING = "Paris"


def get_weather() -> None:
    try:
        weather = requests.get(URL + f"key={API_KEY}&q={FILTERING}")

        if weather.status_code == 200:

            print(f"Performing request to Weather API for city {FILTERING}...")
            data = weather.json()

            print(
                data["location"]["name"],
                "/",
                data["location"]["country"],
                data["location"]["localtime"],
                "Weather: ",
                data["current"]["temp_c"],
                "Celsius, ",
                data["current"]["condition"]["text"],
            )
        else:
            print(f"Error: {weather.status_code}")

    except RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_weather()
