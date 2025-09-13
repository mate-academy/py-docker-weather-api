import os
import requests
import sys

API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    if not API_KEY:
        print("Error: API_KEY environment variable is not set")
        sys.exit(1)

    response = requests.get(
        URL,
        params={
            "key": API_KEY,
            "q": FILTERING,
            "aqi": "no",
        },
    )
    response.raise_for_status()

    data = response.json()

    location = data["location"]
    current = data["current"]

    print(f'Weather in {location["name"]}, {location["country"]}: ')
    print(f'Temperature: {current["temp_c"]}°C')
    print(f'Condition: {current["condition"]["text"]}')
    print(f'Humidity: {current["humidity"]}%')
    print(f'Wind: {current["wind_kph"]} km/h')


if __name__ == "__main__":
    get_weather()
