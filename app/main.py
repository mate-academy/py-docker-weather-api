import os

import requests as requests

URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    try:
        result = requests.get(URL, params={"q": FILTERING, "key": API_KEY})
        data = result.json()
        print(f'{data["location"]["name"]}/{data["location"]["country"]} '
              f'{data["location"]["localtime"]} '
              f'Weather: {data["current"]["temp_c"]} Celsius, '
              f'{data["current"]["condition"]["text"]}')

    except Exception as e:
        print("Exception (weather):", e)
        pass


if __name__ == "__main__":
    get_weather()
