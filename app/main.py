import os
import requests


def get_weather() -> None:
    api_key = os.getenv("WEATHER_API_KEY")
    base_url = "http://api.weatherapi.com/v1/current.json"
    city = "Paris"

    print(f"Performing request to Weather API for city {city}...")

    params = {"key": api_key, "q": city}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        location = data["location"]
        current = data["current"]

        print(
            f"{location['name']}/{location['country']} "
            f"{location['localtime']} "
            f"Weather: {current['temp_c']} Celsius, "
            f"{current['condition']['text']}"
        )
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    get_weather()
