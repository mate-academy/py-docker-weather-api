import os

import requests as requests

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    res = requests.get(URL + f"?q={FILTERING}&key={API_KEY}")
    content = res.json()
    location = content["location"]
    current = content["current"]
    print(f"{location['name']}/{location['country']} "
          f"{location['localtime']} "
          f"Weather: {current['temp_c']} Celsius, "
          f"{current['condition']['text']}")


if __name__ == "__main__":
    get_weather()
