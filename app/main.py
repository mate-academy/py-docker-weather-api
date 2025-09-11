import os
import requests

from dotenv import load_dotenv
load_dotenv()

CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise Exception("API_KEY environment variable is not set")

    full_url = f"{URL}?key={api_key}&q={CITY}"
    response = requests.get(full_url, timeout=5)
    response.raise_for_status()

    data = response.json()

    location = data["location"]["name"]
    country = data["location"]["country"]
    time = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{location}/{country} {time} Weather: {temp_c}°C, {condition}")


if __name__ == "__main__":
    get_weather()
