import os
import requests


URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        raise RuntimeError("API_KEY not provided!")

    params = {"key": api_key, "q": CITY}

    response = requests.get(URL, params=params)
    response.raise_for_status()

    data = response.json()
    print(data)


if __name__ == "__main__":
    get_weather()
