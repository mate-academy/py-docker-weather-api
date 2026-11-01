import os

import requests


API_KEY = os.environ.get("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    response = requests.get(URL + f"?key={API_KEY}&q={FILTERING}")
    data = response.json()
    print(
        f"Weather in {FILTERING}: {data['current']['temp_c']}°C,"
        f" {data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
