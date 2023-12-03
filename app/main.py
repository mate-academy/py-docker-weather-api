import os
import requests

URL = ("http://api.weatherapi.com/v1/current."
       "json?key=9ed0ea20d5ea4cf2bbd224726230212&q=Paris&aqi=yes")

API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(
        URL,
        params={
            "key": API_KEY,
            "q": "Paris"
        }
    )

    weather_data = response.json()
    localtime = weather_data["location"]["localtime"]
    temp_c = weather_data["current"]["temp_c"]
    condition = weather_data["current"]["condition"]["text"]
    print("Performing request to Weather API for city Paris...")
    print(
        f"Paris/France {localtime} "
        f"Weather: {temp_c} Celsius, "
        f"{condition}"
    )


if __name__ == "__main__":
    get_weather()
