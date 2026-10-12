import os

import requests


API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
TIMEOUT = 10


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError(
            "API_KEY environment variable is not set."
        )

    response = requests.get(
        API_URL,
        params={
            "key": api_key,
            "q": CITY,
        },
        timeout=TIMEOUT,
    )
    response.raise_for_status()

    weather_data = response.json()
    location = weather_data["location"]
    current = weather_data["current"]

    print(f"City: {location['name']}")
    print(f"Country: {location['country']}")
    print(f"Temperature: {current['temp_c']}°C")
    print(f"Condition: {current['condition']['text']}")
    print(f"Humidity: {current['humidity']}%")
    print(f"Wind: {current['wind_kph']} km/h")


if __name__ == "__main__":
    get_weather()
