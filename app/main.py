import os

import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    city = "Paris"
    print(f"Performing request to Weather API for city {city}...")

    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        location = data["location"]
        current = data["current"]
        print(f"{location['name']}/{location['country']}: "
              f"{current['last_updated']} "
              f"Weather: {current['temp_c']} Celsius, "
              f"{current['condition']['text']}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    get_weather()
