import os

import requests


API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def parse_weather_data(weather_data: dict) -> str:
    try:
        city = weather_data["location"]["name"]
        country = weather_data["location"]["country"]
        local_time = weather_data["location"]["localtime"]
        temperature = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]

        return (
            f"{city}/{country} {local_time} "
            f"Weather: {temperature} Celsius, {condition}"
        )
    except KeyError as e:
        return f"Missing data in response: {e}"


def get_weather() -> None:
    try:
        weather_response = requests.get(f"{URL}key={API_KEY}&q={FILTERING}")
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        print(parse_weather_data(weather_data))
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
