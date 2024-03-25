import os

import requests

URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Kyiv"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:

    result = requests.get(URL, {"key": API_KEY, "q": FILTERING})

    if result.status_code == 200:
        print("Performing request to weather API for city Kyiv...")
        result = result.json()
        location = result["location"]
        weather = result["current"]
        data = (
            f"{location['name']}/{location['country']} "
            f"{location['localtime']} "
            f"Weather: {weather['temp_c']} Celsius, "
            f"{weather['condition']['text']}"
        )
        print(data)
    else:
        print("No weather data")


if __name__ == "__main__":
    get_weather()
