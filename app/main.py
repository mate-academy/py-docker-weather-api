import os

import requests

URL = "http://api.weatherapi.com/v1/current.json"
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
PAYLOAD = {
    "key": WEATHER_API_KEY,
    "q": "Paris"
}


def get_weather() -> None:
    res = requests.get(URL, params=PAYLOAD).json()
    print(WEATHER_API_KEY)
    location = res["location"]
    temperature = res["current"]["temp_c"]
    condition = res["current"]["condition"]["text"]

    print(
        f"{location['name']}/{location['country']} {location['localtime']} "
        f"Weather: {temperature} Celcius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
