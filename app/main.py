import os
import sys
import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("ERROR: API_KEY environment variable is not set")
        sys.exit(1)

    city = os.getenv("CITY", "Paris")

    params = {
        "key": api_key,
        "q": city,
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("Error fetching weather data:", response.text)
        sys.exit(1)

    data = response.json()

    location = data["location"]
    current = data["current"]
    condition = current["condition"]

    city_name = location["name"]
    temp = current["temp_c"]
    weather = condition["text"]

    print(f"City: {city_name}")
    print(f"Temperature: {temp}°C")
    print(f"Weather: {weather}")


if __name__ == "__main__":
    get_weather()
