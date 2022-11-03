import os
import requests
import json

key = os.environ.get("API_KEY")
prefer_city = "Paris"

# check it on DockerHub
# https://hub.docker.com/r/monobod/py-docker-weather


def get_weather() -> None:
    result = requests.get(
        f"http://api.weatherapi.com/v1/current.json?"
        f"key={key}&q={prefer_city}")

    res = json.loads(result.text)

    city = f"{res['location']['name']}/{res['location']['country']} "
    localtime = f"{res['location']['localtime']} "
    weather = f"Weather: {res['current']['temp_c']} Celsius, " \
              f"{res['current']['condition']['text']}"

    for_printing = city + localtime + weather

    print(for_printing)


if __name__ == "__main__":
    get_weather()
