import os
import sys
import requests


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY") or input("Enter your API key: ")

    params = {
        "key": api_key,
        "q": CITY,
    }

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        data = response.json()

        if data.get("current"):
            weather = data["current"]
            print(f"Current weather in {CITY}:")
            print(f"Temperature: {weather['temp_c']}°C")
            print(f"Condition: {weather['condition']['text']}")
            print(f"Last update: {weather['last_updated']}")

    except requests.exceptions.RequestException as error:
        print(f"Something went wrong: {error}")
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
