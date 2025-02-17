import os

import requests
from requests.exceptions import HTTPError, RequestException
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")

WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"

DEFAULT_CITY = "Paris"


def get_weather_dict_from_weather_api(city_name: str = DEFAULT_CITY) -> dict:
    print(f"Performing request to Weather API for city {city_name}...")
    try:
        response = requests.get(
            WEATHER_API_URL, params={"key": API_KEY, "q": city_name}
        )
        response.raise_for_status()
    except HTTPError as http_err:
        print(http_err)
    except RequestException as req_err:
        print(req_err)
    else:
        return response.json()


def weather_dict_to_string(weather_dict: dict) -> str:
    city = weather_dict["location"]["name"]
    country = weather_dict["location"]["country"]

    datetime = weather_dict["current"]["last_updated"]
    temp_c = weather_dict["current"]["temp_c"]
    outlook = weather_dict["current"]["condition"]["text"]

    return f"{city}/{country} {datetime} Weather {temp_c} Celsius, {outlook}"


def get_weather(
        get_weather_dict: callable,
        **kwargs,
) -> None:
    weather_dict = get_weather_dict(**kwargs)
    try:
        weather_string = weather_dict_to_string(weather_dict)
        print(weather_string)
    except KeyError as e:
        print(e)


if __name__ == "__main__":
    get_weather(get_weather_dict_from_weather_api)
