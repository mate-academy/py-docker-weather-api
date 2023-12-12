import os

import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(url=URL, params={"key": API_KEY, "q": CITY})
    print(f"Response status: {response.status_code}")
    if response.status_code == 200:
        weather_j = response.json()

        print(f"Name: {weather_j['location']['name']}"
              f" Country: {weather_j['location']['country']}"
              f" Localtime: {weather_j['location']['localtime']}"
              f" Temperature: {weather_j['current']['temp_f']} Franklin"
              f" Condition text: {weather_j['current']['condition']['text']}")
    else:
        print(
            f"A status code == {response.status_code}",
            "please try again later"
        )


if __name__ == "__main__":
    get_weather()
