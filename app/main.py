import os
import requests


URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")

    params = {
        "key": api_key,
        "q": CITY,
    }

    print(f"Performing request to Weather API for city {CITY}...")

    response = requests.get(URL, params=params)
    data = response.json()

    location = data["location"]
    current = data["current"]

    city = location["name"]
    country = location["country"]
    local_time = location["localtime"]
    temp = current["temp_c"]
    condition = current["condition"]["text"]

    print(
        f"{city}/{country} {local_time} Weather: {temp} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
