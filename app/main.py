import os
import sys
import requests


CITY = "Paris"
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:

    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API_KEY environment variable is not set.")
        sys.exit(1)

    params = {
        "key": api_key,
        "q": CITY
    }

    temp_c = "temp_c"
    condition = "condition"
    text = "text"
    humidity = "humidity"
    wind_kph = "wind_kph"

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        if "current" in data:
            weather = data["current"]
            print(f"Current weather in {CITY}: ")
            print(f"Temperature: {weather[temp_c]}°C")
            print(f"Condition: {weather[condition][text]}")
            print(f"Humidity: {weather[humidity]}%")
            print(f"Wind Speed: {weather[wind_kph]} kph")
        else:
            print("Error: Unexpected response format.")
            sys.exit(1)

    except requests.exceptions.RequestException as error:
        print(f"Error fetching weather data: {error}")
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
