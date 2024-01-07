import os

import requests

URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {
        "key": os.environ.get("API_KEY"),
        "q": "Paris",
    }

    result = requests.get(URL, params=params)
    my_data = result.json()

    print(
        f"{my_data['location']['name']}/{my_data['location']['country']} "
        f"{my_data['location']['localtime']} "
        f"Weather: {my_data['current']['temp_c']} Celsius, "
        f"{my_data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
