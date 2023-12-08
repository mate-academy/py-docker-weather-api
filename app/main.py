import os
from datetime import datetime, timedelta
import pycountry
import requests
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.openweathermap.org/data/2.5/weather"
CITY = "Paris"
API_KEY = os.environ.get("WEATHER_API_KEY")


def get_weather(
        url: str = URL,
        city: str = CITY,
        api_key: str = API_KEY
) -> None:
    request_parameters = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    print(f"Performing request to Open Weather Map API for city {city}...")
    response = requests.get(url, params=request_parameters)
    if response.status_code == 200:
        data = response.json()
        current_time = (datetime.utcnow() + timedelta(
            seconds=data.get("timezone", 0)
        )).strftime("%Y-%m-%d %H:%M")
        country = pycountry.countries.get(alpha_2=data["sys"]["country"])
        print(f"{data['name']}/{country.name} {current_time} "
              f"Weather: {round(data['main']['temp'], 1)} Celsius, "
              f"{'/'.join(w.get('main', '') for w in data['weather'])}")
    else:
        print("Failed to retrieve weather data. "
              f"Status Code: {response.status_code}")


if __name__ == "__main__":
    get_weather()
