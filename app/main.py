import os
import requests


WEATHER_API = os.environ.get("API_KEY", "1a61cecd1bb949cfa8d150443222811")
CURRENT_WEATHER_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
PARAMS = {"key": WEATHER_API, "q": CITY}


def get_weather() -> None:
    response = requests.get(
        CURRENT_WEATHER_URL, params=PARAMS
    )
    data = response.json()

    location = CITY + "/" + data["location"]["country"]
    localtime = data["location"]["localtime"]
    temp_c = str(data["current"]["temp_c"]) + " Celsius"
    condition = data["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {CITY}...")
    print(f"{location} {localtime} Weather: {temp_c}, {condition}")


if __name__ == "__main__":
    get_weather()
