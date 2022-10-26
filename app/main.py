import os

import requests
from dotenv import load_dotenv


API_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    load_dotenv()

    key = os.environ.get("API_KEY")
    city = "Paris"
    parameters = {"key": {key}, "q": {city}}

    response = requests.get(
        API_URL,
        params=parameters
    )
    info = response.json()

    print(
        f"{info['location']['country']}/{info['location']['name']} "
        f"{info['location']['localtime']} "
        f"Weather: {info['current']['temp_c']} Celsius, "
        f"{info['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
