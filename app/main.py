import os
import requests

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        raise EnvironmentError("API_KEY environment variable is not set.")

    params = {
        "key": api_key,
        "q": CITY,
        "aqi": "no",
    }

    response = requests.get(URL, params=params)
    response.raise_for_status()

    data = response.json()

    location = data["location"]
    current = data["current"]

    print(f"Weather in {location['name']}, {location['country']}:")
    print(f"  Temperature : {current['temp_c']}°C"
          f" (feels like {current['feelslike_c']}°C)")
    print(f"  Condition   : {current['condition']['text']}")
    print(f"  Humidity    : {current['humidity']}%")
    print(f"  Wind        : {current['wind_kph']} kph {current['wind_dir']}")
    print(f"  Visibility  : {current['vis_km']} km")
    print(f"  UV Index    : {current['uv']}")


if __name__ == "__main__":
    get_weather()
