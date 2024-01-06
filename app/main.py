import os
import requests

URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(URL, params={"key": API_KEY, "q": CITY}).json()
    location_data = response.get("location")
    temperature_data = response.get("current")
    condition_data = temperature_data.get("condition")
    result = (
        f"{location_data['name']}/{location_data['country']} "
        f"{location_data['localtime']} "
        f"Weather: {temperature_data['temp_c']} "
        f"Celsius, {condition_data['text']}"
    )
    print(f"Executing request to Weather API for city {CITY}...")
    print(result)


if __name__ == "__main__":
    get_weather()
