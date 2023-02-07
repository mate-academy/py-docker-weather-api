from pprint import pprint
import requests


URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = "1bf0f784af8f4c1c8e7144142233001"


def get_weather() -> None:

    querystring = {
        "key": API_KEY,
        "q": FILTERING,
    }
    response = requests.request("GET", url=URL, params=querystring)
    pprint(response.json())


if __name__ == "__main__":
    get_weather()
