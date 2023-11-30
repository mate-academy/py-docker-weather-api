import os
import requests


API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(
        "https://api.weatherapi.com/v1/current.json",
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
