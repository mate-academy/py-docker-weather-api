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
        tz_id = data.get("location", {}).get("tz_id")
        temp_c = round(data.get("current", {}).get("temp_c"))
        condition = data.get("current", {}).get("condition", {}).get("text")
        localtime = data.get("location", {}).get("localtime")
        print(f"{tz_id} {localtime} Weather: {temp_c}°C, {condition}")
    else:
        print("Error fetching weather data")


if __name__ == "__main__":
    get_weather()
