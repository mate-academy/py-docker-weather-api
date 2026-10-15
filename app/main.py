import os
import requests


CITY = "Paris"
URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("API_KEY")


def get_weather() -> dict:
    if not api_key:
        raise ValueError(
            "API_KEY environment variable is not set."
        )
    params = {
        "q": CITY,
        "appid": API_KEY,
        "units": "metric",
    }
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def main() -> None:
    weather = get_weather()
    print(f"\nWeather in {weather['name']}:")
    print(f"Temperature: {weather['main']['temp']} °C")
    print(f"Feels like: {weather['main']['feels_like']} °C")
    print(f"Humidity: {weather['main']['humidity']}%")
    print(f"Conditions: {weather['weather'][0]['description']}")
    print(f"Wind speed: {weather['wind']['speed']} m/s")


if __name__ == "__main__":
    main()
