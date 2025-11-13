import os
import requests

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris, fr"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    params = {"key": api_key, "q": CITY}
    response = requests.get(url=URL, params=params)
    print(response.json())


if __name__ == "__main__":
    get_weather()
