import os

import requests

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY
    }
    response = requests.get(URL, params=params)
    weather_data = response.json()
    weather_data = weather_data["current"]
    print(f"The current weather in {CITY} is "
          f"{weather_data['condition']['text'].lower()}, "
          f"temperature is {weather_data['temp_c']}°C, "
          f"but it feels like {weather_data['feelslike_c']}°C. "
          f"Wind speed is {weather_data['wind_kph']} kilometers per hour.")


if __name__ == "__main__":
    get_weather()
