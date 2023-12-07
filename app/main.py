import os

import requests
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather(
        url: str = URL,
        filtering: str = FILTERING,
        api_key: str = API_KEY
) -> None:
    """Get weather from API and print it."""
    params = {"key": api_key, "q": filtering}
    res = requests.get(url, params=params).json()

    city = res["location"]["name"]
    country = res["location"]["country"]
    temp = res["current"]["temp_c"]
    condition = res["current"]["condition"]["text"]

    print(
        f"""
        City: {city}
        Country: {country}
        Temperature: {temp}°C
        Condition: {condition}
        """
    )


if __name__ == "__main__":
    get_weather()
