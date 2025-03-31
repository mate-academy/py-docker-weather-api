import requests
import os


def get_weather() -> None:
    API_KEY = os.getenv("API_KEY") # noqa
    if API_KEY: # noqa
        r = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Paris") # noqa
        print(r.json()) # noqa


if __name__ == "__main__":
    get_weather()
