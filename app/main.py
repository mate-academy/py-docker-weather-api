import os
import requests


URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    params = {
        "key": api_key,
        "q": "Paris",
        "aqi": "no"
    }
    response = requests.get(URL, params=params)
    data = response.json()

    name = data["location"]["tz_id"]
    local_time = data["location"]["localtime"]
    temperature_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(
        (f"{name} {local_time} "
         f"Weather: {temperature_c} Celsius, {condition}")
    )


if __name__ == "__main__":
    get_weather()
