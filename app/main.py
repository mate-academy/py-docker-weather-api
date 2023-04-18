import os
import requests

CITY = "Paris"
API_KEY = os.environ.get("API_KEY")
WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    parameters = {"key": API_KEY, "q": CITY}
    response = requests.get(WEATHER_API_URL, params=parameters).json()

    country = response["location"]["country"]
    _datetime = response["location"]["localtime"]
    temperature = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]

    print(
        f"{country}/{CITY} {_datetime} "
        f"Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
