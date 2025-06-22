import os
import requests

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    if not API_KEY:
        print("API_KEY not found in environment variables.")
        return

    params = {
        "key": API_KEY,
        "q": CITY,
        "aqi": "no",
    }

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        data = response.json()
        location = data["location"]
        current = data["current"]

        print(
            f"{location['name']}/{location['country']} "
            f"{location['localtime']} "
            f"Weather: {current['temp_c']} Celsius, "
            f"{current['condition']['text']}"
        )
    except requests.RequestException as e:
        print("Failed to fetch weather data:", e)


if __name__ == "__main__":
    get_weather()
