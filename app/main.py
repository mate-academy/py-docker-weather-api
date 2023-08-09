import requests
from dotenv import load_dotenv
import os

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json?"
API_KEY = os.environ["API_KEY"]
CITY = "Paris"


def get_weather() -> None:
    res = requests.get(
        url="https://api.weatherapi.com/v1/current.json",
        params={"key": API_KEY, "q": CITY}
    )
    res = res.json()
    print(f"Weather now in {CITY}:\n"
          f"Now {res['current']['condition']['text']}\n"
          f"Temperature: {res['current']['temp_c']} °C\n"
          f"Feel slike: {res['current']['feelslike_c']} °C\n"
          f"Pressure: {res['current']['pressure_mb']} mb\n"
          f"Wind Speed: {res['current']['wind_kph']} kph")


if __name__ == "__main__":
    get_weather()
