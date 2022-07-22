import os

import requests


API_KEY = os.environ.get("API_KEY")
WEATHER_ENDPOINT = "http://api.weatherapi.com/v1/current.json"

weather_params = {
    "key": API_KEY,
    "q": "Paris",
}


def get_weather():
    print("Performing request to Weather API for city Paris...")

    response = requests.get(WEATHER_ENDPOINT, params=weather_params)
    response_data = response.json()

    paris_time = response_data["location"]["localtime"].split()
    country = response_data["location"]["country"]
    temperature = response_data["current"]["temp_c"]
    condition = response_data["current"]["condition"]["text"]
    city = response_data["location"]["name"]
    weather_info = (
        f"{city}/{country} {paris_time[0]} {paris_time[1]} "
        f"Weather: {temperature} Celsius, {condition}"
    )

    print(weather_info)


if __name__ == "__main__":
    get_weather()
