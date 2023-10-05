import os

import requests

API_KEY = os.environ.get("WEATHER_API_KEY")
CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY
    }

    response = requests.get(URL, params=params)
    data = response.json()

    location = data["location"]["name"]
    temperature = data["current"]["temp_c"]
    wind = data["current"]["wind_kph"]
    condition = data["current"]["condition"]["text"]
    print(
        f"Weather in {location}",
        f"Temperature is {temperature}",
        f"Wind is {wind} km/h",
        f"{condition}"
    )


if __name__ == "__main__":
    get_weather()
