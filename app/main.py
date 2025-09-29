import os
import requests
from dotenv import load_dotenv

FILTERING = "Paris"
load_dotenv()


def fetch_weather(location: str, lang: str = "ru") -> dict:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError(
            "API_KEY is not set. Pass it via environment variable."
        )

    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": location,
        "aqi": "no",
        "lang": lang,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def parse_weather(data: dict) -> tuple[str, float, str]:
    city = data["location"]["name"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    return city, temp_c, condition


def print_weather(city: str, temp_c: float, condition: str) -> None:
    print(f"Weather in {city}: {temp_c}°C, {condition}")


def get_weather(location: str = FILTERING) -> None:
    data = fetch_weather(location)
    city, temp_c, condition = parse_weather(data)
    print_weather(city, temp_c, condition)


if __name__ == "__main__":
    get_weather()
