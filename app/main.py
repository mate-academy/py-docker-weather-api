import os
import requests


URL = "https://api.weatherapi.com/v1/current.json?"
API_KEY = os.environ["API_KEY"]
CITY = "Paris"
PARAMS = {"key": API_KEY, "q": CITY}


def get_weather() -> None:
    response = requests.get(URL, params=PARAMS).json()
    location = response["location"]
    current = response["current"]
    print(
        f"{location['name']}/{location['country']} {location['localtime']} "
        f"Weather: {current['temp_c']} Celsius, {current['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
