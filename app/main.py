import os
import requests


URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
KEY = os.environ.get("API_KEY")

if not KEY:
    raise ValueError("WEATHER_API_KEY environment variable is not set.")

PARAMS = {
    "key": KEY,
    "q": "Paris"
}


def get_weather() -> None:
    result = requests.get(URL, params=PARAMS)

    if result.status_code == 200:
        data = result.json()
        location = data["location"]
        local_time = location["localtime"]
        weather = data["current"]["condition"]["text"]
        temperature = data["current"]["temp_c"]
        wind = data["current"]["wind_kph"]

        print(f"Weather in {FILTERING}: {weather}, "
              f"Temperature: {temperature}°C, "
              f"Wind kph: {wind},"
              f"Local time: {local_time}")
    else:
        print("Failed to retrieve weather data.")


if __name__ == "__main__":
    get_weather()
