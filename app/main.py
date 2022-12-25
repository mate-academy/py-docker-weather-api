import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(URL, params={"key": API_KEY,
                                         "q": CITY}).json()

    location = response["location"]
    current = response["current"]

    print(f"Country: {location['country']}")
    print(f"City: {location['name']}")
    print(f"Date: {location['localtime']}")
    print(f"Temperature: {current['temp_c']}")
    print(f"Feel Like: {current['feelslike_c']}")
    print(f"Humidity: {current['humidity']}")
    print(f"Wind Speed: {current['wind_mph']}")


if __name__ == "__main__":
    get_weather()
