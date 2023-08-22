import os

import requests

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    params = {
        "key": os.environ["API_KEY"],
        "q": FILTERING
    }
    response = requests.get(URL, params=params)

    if response.status_code == 200:
        data = response.json()
        tz_id = data["location"]["tz_id"]
        temp_c = round(data["current"]["temp_c"])
        condition = data["current"]["condition"]["text"]
        localtime = data["location"]["localtime"]
        print(f"{tz_id} {localtime} Weather: {temp_c}°C, {condition}")
    else:
        print("Error fetching weather data")


if __name__ == "__main__":
    get_weather()
