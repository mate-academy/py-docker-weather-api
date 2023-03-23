import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
CURRENT_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Frankfurt"
AQI = "no"
PARAMS = {"key": f"{API_KEY}", "q": f"{CITY}", "aqi": f"{AQI}"}


def get_weather() -> None:
    current_weather = requests.get(CURRENT_URL, params=PARAMS)
    data = current_weather.json()

    if current_weather.status_code == 200:
        print(
            f"Weather for now in {CITY}:\n"
            f"Now is {int(data['current']['temp_c'])} degrees.\n"
            f"Feels like {int(data['current']['feelslike_c'])} degrees.\n"
            f"Wind speed is {data['current']['wind_kph']} km/h.\n"
            f"Humidity - {data['current']['humidity']}%.\n"
            f"Cloudiness - {data['current']['cloud']}%."
        )
    else:
        print("Something gone wrong :(")


if __name__ == "__main__":
    get_weather()
