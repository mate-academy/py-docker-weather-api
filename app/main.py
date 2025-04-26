import os
import requests


API_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Kyiv"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    params = {
        "key": api_key,
        "q": CITY,
        "aqi": "no"
    }

    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    weather_data = response.json()

    location = weather_data["location"]
    current = weather_data["current"]

    print(f"Weather in {location['name']}, {location['country']}:")
    print(f"Condition: {current['condition']['text']}")
    print(f"Temperature: {current['temp_c']}°C")
    print(f"Feels like: {current['feelslike_c']}°C")
    print(f"Wind: {current['wind_kph']} kph, {current['wind_dir']}")
    print(f"Humidity: {current['humidity']}%")
    print(f"Precipitation: {current['precip_mm']} mm")


if __name__ == "__main__":
    get_weather()
