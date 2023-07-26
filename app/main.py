import os
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
FILTERING = "Paris"


def get_weather() -> None:
    result = requests.get(BASE_URL, params={
        "key": API_KEY,
        "q": FILTERING})

    if result.status_code == 200:
        country = result.json()["location"]["country"]
        city = result.json()["location"]["name"]
        local_time = result.json()["location"]["localtime"]
        temperature = result.json()["current"]["temp_c"]
        condition = result.json()["current"]["condition"]["text"]

        print(
            f"{city}/{country} {local_time} "
            f"Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
