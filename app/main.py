import os
import requests


KEY = os.environ["API_KEY"]
CITY = "Paris"
URL = f"http://api.weatherapi.com/v1/current.json?q={CITY}"


def get_weather() -> None:
    headers = {
        "key": KEY,
    }
    data = requests.get(URL, headers=headers).json()
    country = data["location"]["country"]
    last_updated = data["current"]["last_updated"]
    temp_in_celsius = data["current"]["temp_c"]
    weather_text = data["current"]["condition"]["text"]
    print(
        f"Performing request to Weather API for city {CITY}...\n"
        f"{CITY}/{country} {last_updated} "
        f"Weather: {temp_in_celsius} Celsius, {weather_text}"
    )


if __name__ == "__main__":
    get_weather()
