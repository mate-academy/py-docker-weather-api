import os

import requests


URL = 'http://api.weatherapi.com/v1/current.json'
KEY = os.environ.get('API_KEY')
CITY = 'Paris'


def get_weather() -> dict:

    url = f'{URL}?key={KEY}&q={CITY}&aqi=no'
    response = requests.get(url)
    data = response.json()

    print('Performing request to Weather API to city Paris...')
    print(
        f"{data['location']['name']}/{data['location']['country']} "
        f"{data['location']['localtime']} "
        f"Weather: {data['current']['temp_c']} Celsius, "
        f"{data['current']['condition']['text']}"
    )

    return data


if __name__ == '__main__':
    get_weather()
