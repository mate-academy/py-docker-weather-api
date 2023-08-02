import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("API_KEY")


BASE_URL = "http://api.weatherapi.com/v1"
API_METHOD = "/current.json"
FILTERING = "Paris"


def get_weather() -> str:
    current_weather = (
        requests.get(BASE_URL + API_METHOD + f"?key={API_KEY}&q={FILTERING}").json()
    )
    location = current_weather.pop("location")
    str_location = location.get("name") + "/" + location.get("country")
    data_time = location.get("localtime")
    current_temp = current_weather.get("current")
    temp_c = current_temp.get("temp_c")
    condition = current_temp.get("condition").get("text")
    return f"{str_location} {data_time} Weather: {temp_c} Celsius, {condition}"


if __name__ == "__main__":
    print(f"Performing request to Weather API for city {FILTERING}...")
    print(get_weather())
