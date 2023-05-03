import requests
import os

WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    payload = {"key": API_KEY, "q": CITY}

    response = requests.get(WEATHER_API_URL, payload)

    data = response.json()
    print(f"Current weather for {CITY}:")
    print(f"Temperature: {data['current']['temp_c']} C")
    print(f"Weather condition: {data['current']['condition']['text']}")
    print(f"Wind speed: {data['current']['wind_kph']} km/h")


if __name__ == "__main__":
    get_weather()
