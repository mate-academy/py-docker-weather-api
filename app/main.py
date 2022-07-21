import os

import requests

API_TOKEN = os.environ["API_KEY"]
CITY = os.environ["CITY"]
API_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather():
    req = requests.get(API_URL, params={"key": API_TOKEN,
                                        "q": CITY,
                                        "aqi": "no"})

    response = req.json()
    print(f"{response['location']['name']}/{response['location']['country']} "
          f"{response['current']['last_updated']} "
          f"Weather: {response['current']['temp_c']} °C, "
          f"{response['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
