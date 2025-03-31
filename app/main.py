import os

import requests

URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = os.getenv("CITY", "Paris")


def get_weather() -> None:
    print("Performing request to Weather API for city " + CITY + "...")
    params = {"key": API_KEY, "q": CITY}
    response = requests.get(URL, params=params)
    weather_data = response.json()

    if response.status_code == 200:
        country = weather_data["location"]["country"]
        city = weather_data["location"]["name"]
        time = weather_data["location"]["localtime"]
        temperature = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]
        print(f"{city}/{country} {time} "
              f"Weather: {temperature} Celsius, {condition}")
    else:
        print(weather_data["error"]["message"])


if __name__ == "__main__":
    get_weather()
