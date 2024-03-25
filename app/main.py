import os

import requests

API_KEY = os.environ.get("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/"
CITY = "Paris"


def get_weather() -> str:
    payload = {"key": API_KEY, "q": CITY}
    get_weather_url = BASE_URL + "current.json"
    data = requests.get(get_weather_url, params=payload).json()
    return (f"{data['location']['name']}/{data['location']['country']} "
            f"{data['location']['localtime']} "
            f"Weather: {str(data['current']['temp_c'])} Celsius, "
            f"{data['current']['condition']['text']}")
