import os
import json
import requests


URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")
PARAMS = {
    "q": FILTERING,
    "key": API_KEY,
}


def get_weather() -> None:
    result = requests.get(URL, params=PARAMS)
    json_result = json.loads(result.content)

    date = json_result["location"]["localtime"]
    city = date["location"]["name"]
    country = date["location"]["country"]
    temperature = json_result["current"]["temp_c"]
    condition = json_result["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {city}...")

    print(
        f"{city}/{country} {date} Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
