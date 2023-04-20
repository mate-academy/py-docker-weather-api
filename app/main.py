import os

import requests as requests

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    params = {"key": API_KEY, "q": FILTERING, "aqi": 'no'}
    result = requests.get(URL, params=params)

    if result.status_code == 200:
        weather = result.json()
        temperature = weather["current"]["temp_c"]
        city = weather["location"]["name"]
        country = weather["location"]["country"]
        date = weather["location"]["localtime"]
        description = weather["current"]["condition"]["text"]
        print(f"{city}/{country} {date} {temperature} Celsius {description}")
    else:
        print("Error: can't find information")


if __name__ == "__main__":
    get_weather()
