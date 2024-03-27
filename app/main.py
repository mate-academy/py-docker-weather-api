import os
import requests


API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"


def get_weather() -> None:
    response = requests.get(URL)
    data = response.json()
    celsius = data["current"]["temp_c"]
    print(f"In {CITY}: {celsius} now")


if __name__ == "__main__":
    get_weather()
