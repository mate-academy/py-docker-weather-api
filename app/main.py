import os
import requests

API_KEY = os.environ["API_KEY"]
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY,
        "aqi": "no"
    }

    response = requests.get(URL, params=params)
    response.raise_for_status()

    data = response.json()
    location = data["location"]
    current = data["current"]

    print(f"Location: {location['name']}, {location['country']}")
    print(f"Temperature: {current['temp_c']}°C /"
          f" {current['temp_f']}°F")
    print(f"Feels like: {current['feelslike_c']}°C")
    print(f"Condition: {current['condition']['text']}")
    print(f"Humidity: {current['humidity']}%")
    print(f"Wind: {current['wind_kph']} kph {current['wind_dir']}")


if __name__ == "__main__":
    get_weather()
