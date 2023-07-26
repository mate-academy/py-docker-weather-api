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
            "q": "Paris"
        }
    )

    data = response.json()
    city = data.get("location")["name"]
    country = data.get("location")["country"]
    date = data.get("location")["localtime"]
    temperature = data.get("current")["temp_c"]
    condition = data.get("current")["condition"]["text"]
    print(
        f"{city}/{country} {date} "
        f"Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
