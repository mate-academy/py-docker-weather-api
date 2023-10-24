import os
import requests

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
COUNTRY = "France"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    payload = {"q": CITY, "key": API_KEY}

    request = requests.get(URL, params=payload)
    weather_data = request.json()
    localtime = weather_data["location"]["localtime"]
    temp_c = weather_data["current"]["temp_c"]
    condition = weather_data["current"]["condition"]["text"]
    print(f"Performing request to Weather API for city {CITY}...")
    print(
        f"{CITY}/{COUNTRY} {localtime} "
        f"Weather: {temp_c} Celsius, "
        f"{condition}"
    )


if __name__ == "__main__":
    get_weather()
