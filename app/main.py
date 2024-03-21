import os

import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    url = "http://api.weatherapi.com/v1/current.json"
    filtering = "Paris"
    params = {
        "key": api_key,
        "g": filtering
    }

    result = requests.get(url, params=params)

    weather_data = result.json()
    city = weather_data["location"]["name"]
    country = weather_data["location"]["country"]
    date = weather_data["location"]["localtime"]
    temperature = weather_data["current"]["temp_c"]
    condition = weather_data["current"]["condition"]["text"]
    print(f"{city}/{country} {date} "
          f"Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
