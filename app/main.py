import os
import requests


URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(
        URL,
        params={
            "key": API_KEY,
            "q": CITY,
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
        f"{city}/{country} {localtime} "
        f"Weather: {temp_c} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
