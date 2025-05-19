import os
import requests

BASE_URL = "http://api.weatherapi.com/v1"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable not set!")

    requested_city = "Paris"

    print(f"Performing request to Weather API for city {requested_city}...")

    current_weather = requests.get(
        f"{BASE_URL}/current.json",
        params={
            "q": requested_city,
            "key": api_key  # key param for WeatherAPI.com
        }
    )

    if current_weather.status_code == 200:
        data = current_weather.json()
        location = data["location"]
        current = data["current"]

        city = location["name"]
        country = location["country"]
        date = location["localtime"]
        weather = current["temp_c"]
        weather_description = current["condition"]["text"]

        print(
            f"{city}/{country} {date} "
            f"Weather: {weather}°C, {weather_description}"
        )
    else:
        print("Failed to fetch weather data:", current_weather.text)


if __name__ == "__main__":
    get_weather()
