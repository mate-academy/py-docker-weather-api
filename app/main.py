import os

import requests

URL = "http://api.weatherapi.com/v1/"

KEY = os.environ.get("API_KEY")

FILTER = "Kharkiv"

METHOD = "current.json"


def get_weather() -> None:
    response = requests.get(f"{URL}{METHOD}", params={"key": KEY, "q": FILTER})
    if response.status_code == 200:
        data = response.json()
        print(f"Current location: {data['location']['name']}\n"
              f"Time: {data['location']['localtime']}\n"
              f"Temperature: {data['current']['temp_c']}")
    else:
        print(f"{response.text}")


if __name__ == "__main__":
    get_weather()
