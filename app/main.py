import os
import sys

import requests

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("Please set API_KEY environment variable")
    sys.exit(1)

CITY = os.getenv("CITY", "Paris")
LANG = os.getenv("LANG", "uk")

URL = "https://api.weatherapi.com/v1/current.json"

PARAMS = {
    "key": API_KEY,
    "q": CITY,
    "lang": LANG
}


def get_weather() -> None:
    response = requests.get(URL, params=PARAMS)

    if response.status_code == 200:
        data = response.json()
        print(f"Місто: {data["location"]["name"]}")
        print(f"Температура: {data["current"]["temp_c"]}°C")
        print(f"Погодні умови: {data["current"]["condition"]["text"]}")
    else:
        print("Помилка при запросі: ", response.status_code, response.text)
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
