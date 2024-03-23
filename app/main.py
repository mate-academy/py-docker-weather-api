import os

import requests
from dotenv import load_dotenv

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Zinkiv"


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY}...")
    response = requests.get(
        URL, params={"key": API_KEY, "q": CITY}
    )
    try:
        weather = response.json().get("current")
        location = response.json().get("location")

        print(f"""
        Country: {location["country"]}
        Region: {location["region"]}
        City: {location["name"]}
        Time: {location["localtime"]}
        {"-" * 22}
        Weather
        Temperature in Celsius: {weather["temp_c"]}
        Temperature in Fahrenheit: {weather["temp_f"]}
        Feels like: {weather["feelslike_c"]}
        Wind speed: {weather["wind_kph"]}km/h
        Wind direction: {weather["wind_dir"]}
        Humidity: {weather["humidity"]}
        Cloud: {weather["cloud"]}
        """)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_weather()
