import os
import requests

API_KEY = os.environ.get("API_KEY")
CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY}...")
    response = requests.get(URL + f"?key={API_KEY}&q={CITY}")
    if response.status_code != 200:
        return None

    weather_data = response.json()
    if weather_data:
        print(
            f"{weather_data['location']['name']}/{weather_data['location']['country']} "
            f"{weather_data['location']['localtime']} "
            f"Weather: {weather_data['current']['temp_c']} Celsius, "
            f"{weather_data['current']['condition']['text']}"
        )
    else:
        print("Failed to get weather data")


if __name__ == "__main__":
    get_weather()
