import requests
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"
QUERY = {"key": os.getenv("API_KEY"), "q": "Paris"}


def get_weather() -> None:
    response = requests.get(URL, params=QUERY).json()

    city = response["location"]["name"]
    country = response["location"]["country"]
    current_time = response["current"]["last_updated"]
    current_temperature = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]

    print(
        f"Performing request to Weather API for city {city}...",
        f"{city}/{country} {current_time} "
        f"Weather: {current_temperature} Celsius, {condition}",
        sep="\n",
    )


if __name__ == "__main__":
    get_weather()
