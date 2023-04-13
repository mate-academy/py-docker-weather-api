import os

import requests

URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    if all([URL, API_KEY, CITY]):
        r = requests.get(URL, params={"key": {API_KEY}, "q": {CITY}})
        if r.status_code == 200:
            data = r.json()
            country = data["location"]["country"]
            city = data["location"]["name"]
            temperature = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            print(f"{country}" 
                  f"\n{city}" 
                  f"\n{round(temperature)}°C" 
                  f"\n{condition}")


if __name__ == "__main__":
    get_weather()
