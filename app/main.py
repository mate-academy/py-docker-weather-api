import os
import requests


API_KEY = os.environ.get("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(URL, params={"key": API_KEY, "q": CITY})
    response.raise_for_status()
    data = response.json()

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
