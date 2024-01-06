import requests
import os
from dotenv import load_dotenv
from typing import Dict


def get_weather() -> Dict[str, any]:
    load_dotenv()

    base_url = os.environ.get("BASE_URL")
    params = {
        "key": os.environ.get("API_KEY"),
        "q": os.environ.get("CITY"),
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    weather_data = get_weather()

    if "location" in weather_data and "current" in weather_data:
        location = weather_data.get("location")
        current = weather_data.get("current")
        print(
            f"{location['name']}/{location['country']} "
            f"{current['last_updated']} "
            f"Weather: {current['temp_c']} °C, "
            f"{current.get('condition')['text']}"
        )
    else:
        print("Failed to retrieve weather data.")
