import os
import sys

import requests

API_KEY = os.getenv("API_KEY")
if API_KEY is None:
    print("You need to provide an api key with"
          " -e APY_KEY=your_key when you run container")
    sys.exit(1)

URL = "https://api.weatherapi.com/v1/current.json?"
CITY = "Paris"


def get_weather() -> str:
    response = requests.get(URL, params={"key": API_KEY, "q": CITY})

    if response.status_code == 200:
        data = response.json()
        country = data["location"]["country"]
        time = data["location"]["localtime"]
        temp = data["current"]["temp_c"]
        weather = data["current"]["condition"]["text"]
        print(f"Performing request to Weather API for city {CITY}...")
        print(f"{CITY}/{country} {time} Weather: {temp} Celsius, {weather}")
        sys.exit(0)

    elif response.status_code == 401:
        print("Wrong API key")
        sys.exit(1)

    else:
        print("Can't access to Weather_API")
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
