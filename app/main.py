from pprint import pprint
import requests
import os


def get_weather() -> None:
    URL = "http://api.weatherapi.com/v1/current.json"
    FILTERING = "Paris"

    querystring = {
        "key": os.environ["API_KEY"],
        "q": FILTERING,
    }
    response = requests.request("GET", url=URL, params=querystring)
    pprint(response.json())


if __name__ == "__main__":
    get_weather()
