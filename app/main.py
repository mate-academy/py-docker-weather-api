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
    res = res.json().get("current")
    print(f"Weather now in {CITY}:\n"
          f"Now {res.get('condition').get('text')}\n"
          f"Temperature: {res.get('temp_c')} °C\n"
          f"Feel slike: {res.get('feelslike_c')} °C\n"
          f"Pressure: {res.get('pressure_mb')} mb\n"
          f"Wind Speed: {res.get('wind_kph')} kph")


if __name__ == "__main__":
    get_weather()
