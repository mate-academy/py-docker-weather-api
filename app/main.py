import os

import requests


BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    # write your code here
    if not API_KEY:
        print("Please set 'API_KEY' environment variable")
    else:
        response = requests.get(
            BASE_URL + "?key=" + API_KEY + "&q=" + CITY
        ).json()
        location = response["location"]
        current_weather = response["current"]
        print(f"Current weather for {location['name']}")
        print(f"Current temperature: {current_weather['temp_c']}°C")
        print(f"Feels like: {current_weather['feelslike_c']}°C")
        print(f"Condition: {current_weather['condition']['text']}")
        print(f"Wind speed: {current_weather['wind_kph']} km/h")
        print(
            f"Wind direction: {current_weather['wind_dir']} "
            f"({current_weather['wind_degree']}°)"
        )
        print(f"Pressure: {current_weather['pressure_mb']} mBar")
        print(f"Humidity: {current_weather['humidity']}%")
        print(f"Clouds: {current_weather['cloud']}%")
        print(f"Visibility: {current_weather['vis_km']} km")
        print(f"UV-index: {current_weather['uv']}")


if __name__ == "__main__":
    get_weather()
