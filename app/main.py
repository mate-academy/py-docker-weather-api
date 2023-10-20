import os
import requests


API_KEY = os.environ.get("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
FILTER = "Paris"


def get_weather() -> None:
    query_param = {
        "key": API_KEY,
        "q": FILTER
    }

    response = requests.get(URL, params=query_param)

    if response.status_code == 200:
        data = response.json()
        city = data["location"]["name"]
        country = data["location"]["country"]
        time = data["location"]["localtime"]
        temp_cels = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print("Performing request to Weather API for city Paris...")
        print(f"{city}/{country} {time} Weather: {temp_cels} Celsius, {condition}")

    else:
        print(f"Bad request: {response.status_code}")


if __name__ == "__main__":
    get_weather()
