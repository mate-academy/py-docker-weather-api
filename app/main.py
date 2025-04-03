import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    city = "Paris"

    if not api_key:
        print("API_KEY is not set")
        return

    url = "http://api.openweathermap.org/data/2.5/weather"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]

        print(f"Weather in {city}: {description}, {temperature}°C")

    except requests.RequestException as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    get_weather()
