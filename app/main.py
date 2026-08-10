import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API_KEY is not set in environment variables.")
        return

    params = {
        "key": api_key,
        "q": CITY,
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        city_name = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Weather in {city_name}, {country}: {temp_c}°C, {condition}")
    else:
        print(
            f"Error fetching weather "
            f"({response.status_code}): {response.text}"
        )


if __name__ == "__main__":
    get_weather()
