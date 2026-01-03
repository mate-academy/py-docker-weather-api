import requests
import os

URL = "http://api.weatherapi.com/v1/current.json"
REGION = "Paris"


"""COMMAND=docker pull bossukraine/weather-app:latest"""


def get_weather() -> None:
    # Does use a return command
    if (api_key := os.environ.get("API_KEY")) is None:
        print("API Key not set")

    else:
        print(f"Performing request to Weather API for city {REGION}...")

        params = {"key": api_key, "q": REGION}
        res = requests.get(URL, params=params)
        if res.status_code == 200:
            data = res.json()
            print(
                f"{data['location']['name']}/{data['location']['country']} "
                f"{data['current']['last_updated']} "
                f"Weather: {data['current']['temp_c']} Celsius, {data['current']['condition']['text']}" # noqa E501
            )
        else:
            print(f"{res.status_code} error code")


if __name__ == "__main__":
    get_weather()
