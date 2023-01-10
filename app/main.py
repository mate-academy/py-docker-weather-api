import os

import requests


URL = os.environ["API_KEY"]
FILTERING = "Paris"


def get_weather() -> None:
    data = {
        "key": URL,
        "q": FILTERING,
    }

    request = requests.get("https://api.weatherapi.com/v1/current.json",
                           params=data).json()

    location = request["location"]
    current = request["current"]

    result = {
        "Location": f"{location['name']}, {location['country']}",
        "Temperature": f"{current['temp_c']} °C",
        "Condition": f"{current['condition']['text']}",
        "Wind": f"{current['wind_kph']} km/h",
        "Humidity": f"{current['humidity']} %",
        "Cloudiness": f"{current['cloud']} %"
    }

    print(result)


if __name__ == "__main__":
    get_weather()
