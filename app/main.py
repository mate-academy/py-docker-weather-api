import os
import requests

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
api_key = os.getenv("API_KEY")


def get_weather() -> None:
    payload = {"q": FILTERING, "key": api_key}

    request = requests.get(URL, params=payload)
    weather_data = request.json()
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
