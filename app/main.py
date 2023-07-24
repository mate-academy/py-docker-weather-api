import requests
from dotenv import load_dotenv
import os

load_dotenv()


def get_weather(city_name: str, api_key: str) -> dict:
    base_url = "https://api.weatherapi.com/v1/current.json"
    params = {"q": city_name, "key": api_key}

    response = requests.get(base_url, params=params)
    data = response.json()
    return data


if __name__ == "__main__":
    weather = get_weather("Paris", os.getenv("API_KEY"))
    print(
        "Performing request to Weather API for city "
        f"{weather['location']['name']}..."
    )
    print(
        f"{weather['location']['name']}/{weather['location']['country']} "
        f"{weather['location']['localtime']} "
        f"{weather['current']['temp_c']} Celsius "
        f"{weather['current']['condition']['text']}"
    )
