import requests
import os
from dotenv import load_dotenv

FILTERING = "Paris"
URL = "http://api.weatherapi.com/v1/current.json?key="
KEY = os.environ.get("KEY")
load_dotenv()


def get_weather() -> str:
    response = requests.get(URL + f"{KEY}&q=" + f"{FILTERING}&api=no")
    weather_data = response.json()
    temperature = weather_data.get("current")["temp_c"]
    return f"The temperature in {FILTERING} is {temperature} degrees Celsius"


if __name__ == "__main__":
    print(get_weather())
