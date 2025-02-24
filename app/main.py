import os
import requests

API_KEY = os.getenv("WEATHER_API_KEY")

CITY = "Paris"
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {"key": API_KEY, "q": CITY, "aqi": "no"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        current = data["current"]
        location = data["location"]

        print(
            f"Weather in {location['name']}, {location['region']}, "
            f"{location['country']}: {current['condition']['text']}")
        print(f"Temperature: {current['temp_c']}°C (Feels like: "
              f"{current['feelslike_c']}°C)")
        print(f"Humidity: {current['humidity']}%")
        print(f"Wind: {current['wind_kph']} kph "
              f"({current['wind_dir']})")
        print(f"Pressure: {current['pressure_mb']} mb")
        print(f"Visibility: {current['vis_km']} km")
    else:
        print(f"Failed to get weather data: {response.status_code}, "
              f"{response.text}")


if __name__ == "__main__":
    get_weather()
