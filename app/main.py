import os
import requests

API_KEY = os.environ.get("API_KEY")

BASE_URL = "https://api.weatherapi.com/v1/current.json"

params = {
    "q": "Paris",
    "key": API_KEY
}


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        json_data = response.json()
        city = json_data["location"]["name"]
        country = json_data["location"]["country"]
        localtime = json_data["location"]["localtime"]
        temp_c = json_data["current"]["temp_c"]
        condition = json_data["current"]["condition"]["text"]

        print(
            f"{city}/{country} {localtime} "
            f"Weather: {temp_c} Celsius, {condition}"
        )
    else:
        print(f"Request failed with status code {response.status_code}")


if __name__ == "__main__":
    get_weather()
