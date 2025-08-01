import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "Paris"


def get_weather() -> None:
    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": CITY,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        weather = data["current"]
        country = data["location"]["country"]
        localtime = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        weather_condition = weather["condition"]["text"]
        wind_speed = weather.get("wind_kph")

        print(f"Paris, {country}")
        print(f"Local time: {localtime}")
        print(f"Temperature: {temperature}")
        print(f"{weather_condition}")
        print(f"Wind speed: {wind_speed} km/h")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data {e}")


if __name__ == "__main__":
    get_weather()
