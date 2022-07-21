import datetime
import os

import requests


def get_weather(requests_city):
    url = "http://api.weatherapi.com/v1/current.json"

    try:
        api_key = os.getenv("API_KEY", default=None)
        parameters = {
            "key": api_key,
            "q": requests_city,
        }
        response = requests.get(url, params=parameters).json()
    except TypeError:
        print("you should give an api_key")
        return



    city = response["location"]["name"]
    country = response["location"]["country"]
    time = datetime.datetime.strptime(
        response["location"]["localtime"], "%Y-%m-%d %H:%M"
    )
    temperature = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]

    print(
        f"{city}({country}): forecast for {time.date()}"
        f" is {temperature}°C, ({condition})"
    )


if __name__ == "__main__":
    get_weather(
        requests_city = "Paris",
    )
