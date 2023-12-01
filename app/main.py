import os
import requests


CITY = "Paris"
API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    payload = {
        "key": API_KEY,
        "q": CITY
    }
    res = requests.get(
        URL,
        params=payload
    )

    data = res.json()

    location = data.get("location")
    country = location["country"]
    localtime = location["localtime"]

    current_weather = data.get("current")
    temp = current_weather["temp_c"]
    condition = current_weather.get("condition")["text"]

    print(f"Performing request to Weather API for city {CITY}...")
    print(f"{CITY}/{country} {localtime} Weather: {temp} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
