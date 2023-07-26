import os
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
FILTERING = "Paris"


def get_weather() -> None:
    response = requests.get(
        "http://api.weatherapi.com/v1/current.json",
        params={
            "key": os.environ.get("API_KEY"),
            "q": "Paris"}
    ).json()

    city = response.get("location")["name"]
    country = response.get("location")["country"]
    date = response.get("location")["localtime"]
    temperature = response.get("current")["temp_c"]
    condition = response.get("current")["condition"]["text"]

    print(
        f"{city}/{country} {date} "
        f"Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
