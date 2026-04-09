import os
import requests


def get_weather() -> None:
    SECRET_KEY = os.environ.get('API_KEY')
    r = requests.get(f'https://api.weatherapi.com/v1/current.json?q=Paris&key={SECRET_KEY}')
    print(r.json())


if __name__ == "__main__":
    get_weather()
