import os
import requests


API_KEY = os.environ.get("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    params = {"key": API_KEY, "q": CITY}
    res = requests.get(url=URL, params=params)
    if res.status_code == 200:
        print(res.json())
    else:
        print(f"Error: {res.status_code}."
              f"Something wrong with the Weather API request.")


if __name__ == "__main__":
    get_weather()
