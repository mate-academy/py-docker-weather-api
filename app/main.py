import requests
import os
from dotenv import load_dotenv

FILTERING = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"
KEY = os.environ.get("KEY")
load_dotenv()


def get_weather() -> str:
    params = {
        "key": KEY,
        "q": FILTERING,
        "api": "no"
    }

    response = requests.get(URL, params=params)
    weather_data = response.json()
    temperature = weather_data.get("current")["temp_c"]
    return f"The temperature in {FILTERING} is {temperature} degrees Celsius"


if __name__ == "__main__":
    print(get_weather())
