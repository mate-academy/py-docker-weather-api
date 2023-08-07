import os
import requests


CITY = "Paris"
KEY = os.environ["API_KEY"]
URL = f"https://api.weatherapi.com/v1/current.json?q={CITY}"


def get_weather() -> None:
    headers = {
        "key": KEY,
    }

    result = requests.get(URL, headers=headers)

    data = result.json()
    country = data["location"]["country"]
    last_updated = data["current"]["last_updated"]
    temp_c = data["current"]["temp_c"]
    weather_text = data["current"]["condition"]["text"]
    result_string = (f"{CITY}/{country} {last_updated} "
                     f"Weather: {temp_c} Celsius, {weather_text}")
    print(f"Performing request to Weather API for city {CITY}...")
    print(result_string)


if __name__ == "__main__":
    get_weather()
