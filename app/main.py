import os
import requests

URL = "https://api.weatherapi.com/v1/current.json"

API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(
        URL,
        params={
            "key": API_KEY,
            "q": "Paris"
        }
    )

    if response.status_code == 200:
        weather_data = response.json()
        localtime = weather_data["location"]["localtime"]
        temp_c = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]
        print("Performing request to Weather API for city Paris...")
        print(
            f"Paris/France {localtime} \n"
            f"Weather: {temp_c} Celsius, \n"
            f"{condition}"
        )


if __name__ == "__main__":
    get_weather()
