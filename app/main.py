import os

import requests


URL = 'https://api.weatherapi.com/v1/current.json'
CITY = 'Paris'
API_KEY = os.environ['API_KEY']


def get_weather() -> None:
    params = {
        'key': API_KEY,
        'q': CITY,
    }

    response = requests.get(URL, params=params)
    response.raise_for_status()

    data = response.json()

    location = data['location']
    current = data['current']

    print(
        f"{location['name']}/{location['country']} "
        f"{current['last_updated']} "
        f"Weather: {current['temp_c']} Celsius, "
        f"{current['condition']['text']}"
    )


if __name__ == '__main__':
    get_weather()
