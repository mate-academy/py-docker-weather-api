import os

import requests


API_KEY = os.environ.get("API_KEY")
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "PARIS"


def get_weather() -> None:
    request_get = requests.get(
        url=WEATHER_API_URL,
        params={"key": API_KEY, "q": "Paris"}
    )

    if request_get.status_code == 200:
        print(f"Performing request to Weather API for city {CITY}...")

        result = request_get.json()
        location = (f"{result['location']['name']}/"
                    f"{result['location']['country']}")
        localtime = result["location"]["localtime"]
        temp_c = result["current"]["temp_c"]
        condition = result["current"]["condition"]["text"]

        print(f"{location} {localtime} Weather: {temp_c} Celsius, {condition}")

    else:
        print("Invalid request")


if __name__ == "__main__":
    get_weather()
