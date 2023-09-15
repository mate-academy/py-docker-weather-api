import os

import requests


api_key = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:

    response = requests.get(URL, params={"q": FILTERING, "key": api_key})

    if response.status_code == 200:
        data = response.json()
        print(
            f"Weather in {FILTERING}: {data['current']['temp_c']}°C,"
            f" {data['current']['condition']['text']}"
        )
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    get_weather()
