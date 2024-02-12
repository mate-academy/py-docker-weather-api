import os

import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    url = "http://api.weatherapi.com/v1/current.json"
    filtering = "Paris"

    result = requests.get(url + f"?key={api_key}&q={filtering}")

    weather_data = result.json()
    location = (weather_data["location"]["name"]
                + "/"
                + weather_data["location"]["country"])
    date = weather_data["location"]["localtime"]
    temperature, condition = (weather_data["current"]["temp_c"],
                              weather_data["current"]["condition"]["text"])
    print(f"{location} {date} Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
