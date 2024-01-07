import os

import requests

URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {
        "key": os.environ.get("API_KEY"),
        "q": "Paris",
    }

    result = requests.get(URL, params=params)
    result.raise_for_status()
    my_data = result.json()

    print(
        f"{my_data.get('location').get('name')}/"
        f"{my_data.get('location').get('country')} "
        f"{my_data.get('location').get('localtime')} "
        f"Weather: {my_data.get('current').get('temp_c')} Celsius, "
        f"{my_data.get('current').get('condition').get('text')}"
    )


if __name__ == "__main__":
    get_weather()
