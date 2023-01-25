import os
import requests

from dotenv import load_dotenv


load_dotenv()


URL = "https://api.weatherapi.com/v1/current.json"

API_KEY = os.getenv("API_KEY")
FILTERING = "Paris"

PARAMS = {"key": API_KEY, "q": FILTERING}


def get_weather() -> None:

    response = requests.get(url=URL, params=PARAMS).json()

    location = response["location"]
    current = response["current"]

    print(
        f"Performing request to Weather API for city {location['name']}...\n"
        f"{location['name']}/{location['country']} {location['localtime']} "
        f"Weather: {current['temp_c']}°C, {current['condition']['text']}."
    )


if __name__ == "__main__":
    get_weather()
