import os
import requests
from dotenv import load_dotenv

FILTERING = "Paris"
load_dotenv()


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError(
            "API_KEY is not set. Pass it via environment variable."
        )

    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": FILTERING,
        "aqi": "no"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    city = data["location"]["name"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Weather in {city}: {temp_c}°C, {condition}")


if __name__ == "__main__":
    get_weather()
