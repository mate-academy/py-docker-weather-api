import os

import requests


def get_weather() -> None:
    response = requests.get(
        "http://api.weatherapi.com/v1/current.json",
        params={
            "key": os.environ.get("API_KEY"),
            "q": "Paris"
        })

    if response.status_code == 200:
        data = response.json()

        city = data["location"]["name"]
        region = data["location"]["region"]
        country = data["location"]["country"]
        localtime = data["location"]["localtime"]
        wind_kph = data["wind_kph"]
        wind_dir = data["wind_dir"]
        humidity = data["humidity"]
        cloud = data["cloud"]

        print(
            f"City {city}"
            f"Region {region}"
            f"Country {country}"
            f"Local Time {localtime}"
            f"Wind speed in kilometer per hour {wind_kph}"
            f"Wind direction {wind_dir}"
            f"Humidity {humidity}"
            f"Cloud cover {cloud}"
        )
    else:
        print(
            f"Your personal token is not valid"
            f"Please, regenerate new and try again!"
            f"Status code {response.status_code}")


if __name__ == "__main__":
    get_weather()
