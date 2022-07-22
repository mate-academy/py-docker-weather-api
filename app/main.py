import os

import requests


def get_api_response(city: str, api_key: str):
    payload = {
        "key": api_key,
        "q": city
    }
    url = "http://api.weatherapi.com/v1/current.json"

    response = requests.get(url, params=payload)

    return response.json()


def get_weather():
    city = "Kharkiv"
    api_key = os.environ["API_KEY"]

    res = get_api_response(city, api_key)
    country = res["location"]["country"]
    local_time = res["location"]["localtime"]
    temperature = res["current"]["temp_c"]
    weather = res["current"]["condition"]["text"]
    result = f"{city}/{country} {local_time} Weather: {temperature} " \
             f"Celsius, {weather}"
    print(result)


if __name__ == "__main__":
    get_weather()
