import os

import requests

# os.environ["API_KEY"] = "7c50588873ce40198ea125550242503"
API_KEY = os.environ.get("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {"key": API_KEY, "q": "Paris"}

    data = requests.get(URL, params).json()

    country = data["location"]["country"]
    time = data["current"]["last_updated"]
    temperature = data["current"]["temp_c"]
    weather = data["current"]["condition"]["text"]

    print(
        f"Country: {country}\n"
        f"City: Paris\n"
        f"Time: {time}\n"
        f"Temperature: {temperature}\n"
        f"Weather: {weather}"
    )


if __name__ == "__main__":
    get_weather()
