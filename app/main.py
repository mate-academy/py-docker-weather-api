import requests
import os

API_KEY = os.getenv("API_KEY")
CITY_NAME = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("Error. Couldn't fetch weather.")

    response = requests.get(URL, params={"key": API_KEY, "q": CITY_NAME})
    weather_data = response.json()
    print(
        f"{weather_data.get('location').get('name')}/"
        f"{weather_data.get('location').get('country')} "
        f"{weather_data.get('location').get('localtime')} "
        f"Weather: {weather_data.get('current').get('temp_c')} Celsius, "
        f"{weather_data.get('current').get('condition').get('text')}"
    )


if __name__ == "__main__":
    get_weather()
