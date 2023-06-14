import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")
FILTERING = "Barcelona"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    response = requests.get(URL, params={"key": API_KEY, "q": FILTERING})

    if response.status_code == 200:
        response = response.json()

        city = response["location"]["name"]
        country = response["location"]["country"]
        localtime = response["location"]["localtime"]
        condition = response["current"]["condition"]["text"]

        temperature = response["current"]["temp_c"]
        feelslike_c = response["current"]["feelslike_c"]
        humidity = response["current"]["humidity"]
        wind_kph = response["current"]["wind_kph"]

        print(
            f"The weather in {city}, {country} "
            f"(local time: {localtime}) is {condition}\n"
            f"Temperature: {temperature}°C\n"
            f"Feels like {feelslike_c}°C\n"
            f"Humidity: {humidity}\n"
            f"Wind: {wind_kph} km/h"
        )


if __name__ == "__main__":
    get_weather()
