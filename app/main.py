import os
import requests

CITY = "Paris"
API_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise Exception("API_KEY environment variable is not set")
    params = {
        "key": api_key,
        "q": CITY,
    }
    res = requests.get(API_URL, params=params)
    data = res.json()
    print(
        f"{data['location']['name']}/"
        f"{data['location']['country']}"
        f" {data['location']['localtime']}"
        f" Weather: {data['current']['temp_f']}"
        f" {data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
