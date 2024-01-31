import os

import requests


def get_weather() -> None:
    key = str(os.environ.get("APIKEY"))

    res = requests.get("http://api.weatherapi.com/v1/current.json", params={
        "key": key,
        "q": "Kyiv"
    })
    print(f"Kyiv temperature "
          f"{res.json()['current']['temp_c']},"
          f" {res.json()['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
