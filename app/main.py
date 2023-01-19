from pprint import pprint
import requests
import os


def get_weather() -> None:
    url = "http://api.weatherapi.com/v1/current.json"
    filtering = "Paris"
    # First I used uppercase as advise
    # in best practice but flake8 did not pass

    querystring = {
        "key": os.environ["API_KEY"],
        "q": filtering,
    }
    response = requests.request("GET", url=url, params=querystring)
    pprint(response.json())


if __name__ == "__main__":
    get_weather()
