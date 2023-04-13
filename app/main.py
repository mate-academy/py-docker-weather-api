import os

import requests

API_KEY = os.environ.get("API_KEY")

URL = f"http://api.weatherapi.com/v1/current.json?ket={API_KEY}&"
FILTERING = "Paris"


def get_weather() -> None:
    parameters = {
        "key": API_KEY,
        "q": FILTERING
    }

    output = requests.get(URL, params=parameters)

    print(output.content)


if __name__ == "__main__":
    get_weather()
