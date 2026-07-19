import requests
import os
from dotenv import load_dotenv


load_dotenv()
URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.getenv("API_KEY")

params = {
    "key": API_KEY,
    "q": CITY,
    "aqi": "no",
    "lang": "en",
}


def get_weather() -> None:

    res = requests.get(URL, params=params, timeout=10)
    res.raise_for_status()

    data = res.json()

    location = data["location"]
    current = data["current"]
    print(f"City: {location['name']}")
    print(f"Country: {location['country']}")
    print(f"Temperature: {current['temp_c']} °C")
    print(f"Condition: {current['condition']['text']}")
    print(f"Humidity: {current['humidity']}%")
    print(f"Wind: {current['wind_kph']} km/h")


if __name__ == "__main__":
    get_weather()
