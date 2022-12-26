import os

import requests


WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
PAYLOAD = {
    "key": API_KEY,
    "q": "Paris",
}


def get_weather() -> None:
    response = requests.post(WEATHER_API_URL, data=PAYLOAD)
    weather_api_data = response.json()

    country = weather_api_data["location"]["country"]
    city = weather_api_data["location"]["name"]
    time = weather_api_data["current"]["last_updated"]
    temperature = weather_api_data["current"]["temp_c"]
    condition = weather_api_data["current"]["condition"]["text"]

    print(
        f"Performing request to Weather API for city {city}...\n"
        f"{city}/{country} {time} Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
