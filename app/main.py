import requests
import os


BASE_URL = "https://api.weatherapi.com/v1"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"


def get_weather() -> None:

    print(f"Performing request to Weather API for city {CITY}...")

    payload = {"key": API_KEY, "q": CITY}
    result = requests.get(f"{BASE_URL}/current.json", params=payload)
    if result.status_code == 200:
        weather_data = result.json()
        location = weather_data["location"]
        weather = weather_data["current"]
        print(
            f"{location['name']}/{location['country']} "
            f"{location['localtime']} Weather: {weather['temp_c']} Celsius, "
            f"{weather['condition']['text']}"
        )
    else:
        print(f"Invalid request: {result.status_code}")


if __name__ == "__main__":
    get_weather()
