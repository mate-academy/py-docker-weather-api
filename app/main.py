import os
import requests


API_URL = "http://api.openweathermap.org/data/2.5/weather"
CITY = "Paris"
UNITS = "metric"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    params = {
        "q": CITY,
        "appid": api_key,
        "units": UNITS
    }

    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    return response.json()


def main() -> None:
    weather_data = get_weather()
    temp = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    print(f"Current weather in {CITY}: {temp}°C, {description}")


if __name__ == "__main__":
    main()
