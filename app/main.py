import os

import requests

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    if not API_KEY:
        print("API_KEY in not set")
        return

    response = requests.get(
        URL,
        params={
            "key": API_KEY,
            "q": FILTERING
        }
    )

    weather_data = response.json()
    current = weather_data["current"]

    name = weather_data["location"]["name"]
    temp_c = current["temp_c"]
    condition = current["condition"]["text"]
    humidity = current["humidity"]
    wind_kph = current["wind_kph"]

    print(f"City: {name}")
    print(f"Temperature: {temp_c} °C")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity}%")
    print(f"Wind: {wind_kph} km/h")


if __name__ == "__main__":
    get_weather()
