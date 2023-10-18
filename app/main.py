import requests
import os


BASE_URL = "https://api.weatherapi.com/v1"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    if not API_KEY:
        print("No api token set")
        return

    print(f"Performing request to Weather API for city {CITY}...")

    payload = {"key": API_KEY, "q": CITY}
    resp = requests.get(f"{BASE_URL}/current.json", params=payload)
    if resp.status_code == 200:
        weather_data = resp.json()
        location = weather_data["location"]
        weather = weather_data["current"]
        print(
            f"{location['name']}/{location['country']} "
            f"{location['localtime']} Weather: {weather['temp_c']} Celsius, "
            f"{weather['condition']['text']}"
        )
    else:
        print(f"Invalid request: {resp.status_code}")


if __name__ == "__main__":
    get_weather()
