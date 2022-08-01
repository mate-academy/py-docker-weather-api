import requests
import json
import os

# API_KEY=661e47b4f1a34d989df132324222107
API_KEY = os.environ.get("API_KEY")
API_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather():
    if API_KEY is None:
        print("You didn't provide an API_KEY value")
    city = "Paris"
    params = {
        "key": API_KEY,
        "q": city,
    }
    request = requests.get(API_URL, params=params)
    data = json.loads(request.text)
    weather_data = data["current"]
    print(f"The weather in {city}:")
    print(f"Temperature: {weather_data['temp_c']}")
    print(f"Wind: {weather_data['wind_kph']} ({weather_data['wind_dir']})")
    print(f"Humidity: {weather_data['humidity']}")


if __name__ == "__main__":
    get_weather()
