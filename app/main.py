import os
import sys
import requests


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("ERROR: API_KEY is not set")
        sys.exit(1)

    city = "Paris"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Description: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind} m/s")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
