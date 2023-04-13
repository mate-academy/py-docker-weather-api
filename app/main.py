import os
import requests


API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "London"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": FILTERING
    }
    result = requests.get(URL, params=params)
    info = result.json()

    if "location" in info:
        country = info["location"]["country"]
        city = info["location"]["name"]
        condition = info["current"]["condition"]["text"]
        temp = info["current"]["temp_c"]
        wind = info["current"]["wind_kph"]
        date = info["current"]["last_updated"]
        print(
            f"Weather in {city} ({country}): {condition}."
            f"Temperature: {temp}°C."
            f"Wind speed: {wind} km/h."
            f"Last update: {date}."
        )
    else:
        print("No information")


if __name__ == "__main__":
    get_weather()
