import os

import requests


CITY_NAME = "Paris"
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")


def get_weather(city_name: str, weather_api_url: str, api_key: str) -> None:
    if not api_key:
        raise ValueError("API key not provided")

    data = requests.get(
        url=weather_api_url,
        params={
            "key": api_key,
            "q": city_name,
        },
    ).json()
    if error := data.get("error"):
        raise Exception(error)

    result = (
        f"{data.get('location').get('name')}/"
        f"{data.get('location').get('country')} "
        f"{data.get('location').get('localtime')} "
        f"Weather: {data.get('current').get('temp_c')} "
        f"Celsius, {data.get('current').get('condition').get('text')}"
    )
    print(result)


if __name__ == "__main__":
    get_weather(
        city_name=CITY_NAME, weather_api_url=WEATHER_API_URL, api_key=API_KEY
    )
