import os
import requests

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("API_KEY is missing!")
        return

    print(f"Performing request to Weather API for city {CITY}...")

    params = {
        "key": api_key,
        "q": CITY
    }

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error fetching weather: {response.text}")


if __name__ == "__main__":
    get_weather()
