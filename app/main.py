import os
import requests

API_KEY = os.environ.get("API_KEY")
CITY = "Lviv"

WEATHER_API_URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"

def get_weather() -> None:
    response = requests.get(WEATHER_API_URL)
    data = response.json()
    return data

if __name__ == "__main__":
    weather_info = get_weather()
    print(weather_info)
