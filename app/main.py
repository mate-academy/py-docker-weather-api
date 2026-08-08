import os
import requests

CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    response = requests.get(f"{URL}?key={api_key}&q={CITY}")
    data = response.json()
    print(data["location"]["name"])
    print(data["current"]["temp_c"])
    print(data["current"]["condition"]["text"])


if __name__ == "__main__":
    get_weather()
