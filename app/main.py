import os
import requests


API_KEY = "3647e2845af24914ad1111124231304"
FILTERING = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:

    params = {
        "key": API_KEY,
        "q": FILTERING
    }

    response = requests.get(URL, params=params)

    print(response.content)


if __name__ == "__main__":
    get_weather()
