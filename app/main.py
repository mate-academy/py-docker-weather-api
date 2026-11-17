import os
import requests


CITY = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY,
    }
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()
    weather_data = response.json()
    print(f"City: {params['q']}")
    print(f"Temperature: {weather_data['current']['temp_c']} °C")
    print(f"Condition: {weather_data['current']['condition']['text']}")
    print(f"Humidity: {weather_data['current']['humidity']} %")
    print(f"Wind speed: {weather_data['current']['wind_kph']} km/h")


if __name__ == "__main__":
    get_weather()
