import os
import requests as requests


URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
KEY = os.getenv("API_KEY")


def get_weather() -> None:
    data_request = requests.get(f"{URL}?q={CITY}&key={KEY}")
    data = data_request.json()
    location = data["location"]
    current = data["current"]
    print(
        f"{location['name']}/{location['country']} "
        f"{location['localtime']} "
        f"Weather: {current['temp_c']} Celsius, "
        f"{current['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
