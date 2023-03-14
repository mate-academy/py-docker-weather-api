import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")
PARAMS = {"key": API_KEY, "q": FILTERING}


def get_weather() -> None:
    result = requests.get(url=URL, params=PARAMS).json()

    location = result["location"]
    current = result["current"]
    print(
        f"Country: {location['country']}\n"
        f"City: {location['name']}\n"
        f"lat: {location['lat']}, long: {location['lon']}\n"
        f"Time zone: {location['tz_id']}\n"
        f"Local time: {location['localtime']}\n"
    )
    print(
        f"Temperature: {current['temp_c']} C\n"
        f"Condition: {current['condition']['text']}\n"
        f"Wind speed: {current['wind_kph']} km/h\n"
        f"Wind direction: {current['wind_dir']}\n"
        f"Pressure: {current['pressure_mb']} mb\n"
        f"Humidity: {current['humidity']}%"
    )


if __name__ == "__main__":
    get_weather()
