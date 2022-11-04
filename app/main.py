import os
import requests
import json

KEY = os.environ.get("API_KEY")
PREFER_CITY = "Paris"
CURRENT_WEATHER_URL = "http://api.weatherapi.com/v1/current.json?"

# check it on DockerHub
# https://hub.docker.com/r/monobod/py-docker-weather


def get_weather() -> None:
    result = requests.get(CURRENT_WEATHER_URL + f"key={KEY}&q={PREFER_CITY}")

    res = json.loads(result.text)

    city = f"{res['location']['name']}/{res['location']['country']} "
    localtime = f"{res['location']['localtime']} "
    weather = f"Weather: {res['current']['temp_c']} Celsius, " \
              f"{res['current']['condition']['text']}"

    for_printing = city + localtime + weather

    print(for_printing)


if __name__ == "__main__":
    get_weather()
