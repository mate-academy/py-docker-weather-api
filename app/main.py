import os
import requests


BASE_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(
        BASE_URL,
        params={
            "key": API_KEY,
            "q": "Paris",
        },
    )
    data = response.json()
    location = data["location"]
    current = data["current"]

    city = location["name"]
    country = location["country"]
    localtime = location["localtime"]
    temp_c = current["temp_c"]
    condition = current["condition"]["text"]

    print(
        f"{city}/{country} {localtime} Weather: {temp_c} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
