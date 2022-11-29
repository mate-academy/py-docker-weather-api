import os
import requests


WEATHER_URL = "https://api.weatherapi.com/v1/current.json?"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"
PARAMS = {"key": API_KEY, "q": CITY}


def get_weather() -> None:
    res = requests.get(WEATHER_URL, params=PARAMS).json()

    location = f'{res["location"]["name"]}/{res["location"]["country"]}'
    localtime = res["location"]["localtime"]
    temperature = res["current"]["temp_c"]
    wind_speed = res["current"]["wind_kph"]
    condition = res["current"]["condition"]["text"]

    print(
        f"Now in {location} \n"
        f"Localtime: {localtime} \n"
        f"Temperature: {temperature}°C \n"
        f"Wind speed: {wind_speed} km/h \n"
        f"Condition: {condition} \n"
    )


if __name__ == "__main__":
    get_weather()
