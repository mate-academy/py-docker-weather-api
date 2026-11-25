import os
import requests


API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY is not set!")
        return

    params = {
        "key": api_key,
        "q": CITY
    }
    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"Weather API Error: {error}")
        return
    data = response.json()
    current = data["current"]

    print(f"Temperature: {current['temp_c']} °C")
    print(f"Condition: {current['condition']['text']}")
    print(f"Last updated: {current['last_updated']}")


if __name__ == "__main__":
    get_weather()
