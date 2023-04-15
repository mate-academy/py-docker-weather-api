import os
import requests

API_KEY = os.environ.get("API_KEY")
LOCATION = "Paris"
URL = "http://api.weatherapi.com/v1/current.json?"


def get_weather() -> None:
    response = requests.get(f"{URL}key={API_KEY}&q={LOCATION}")
    data = response.json()

    print(f"Performing request to Weather API for city {LOCATION}...")
    location = data.get("location")
    current = data.get("current")
    print(
        f"{location.get('name')}/{location.get('country')} "
        f"{location.get('localtime')} Weather: {current.get('temp_c')} "
        f"Celsius, {current.get('condition').get('text')}"
    )


if __name__ == "__main__":
    get_weather()
