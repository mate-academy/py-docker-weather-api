import os
import sys
import requests


CITY = "Paris"
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError(
            "API_KEY not found in environment variables!"
        )
    params = {
        "key": api_key,
        "q": CITY,
        "lang": "en",
        "aqi": "no"
    }
    response = requests.get(WEATHER_API_URL, params=params)
    if response.status_code != 200:
        print(
            f"Error: "
            f"Weather API returned {response.status_code}: {response.text}"
        )
        sys.exit(1)

    data = response.json()
    print(
        f"Weather in {CITY}: {data['current']['temp_c']}°C, "
        f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
