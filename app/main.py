import os
import requests

WEATHER_API = os.environ.get("WEATHER_API")


URL = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API}"
FILTER_CITY = "Paris"
URL_WITH_PARAMS = URL + f"&q={FILTER_CITY}"


def get_weather() -> None:
    answer = requests.get(URL_WITH_PARAMS).json()
    country = answer["location"]["country"]
    city = answer["location"]["name"]
    datetime_ = answer["location"]["localtime"]
    temp_c = answer["current"]["temp_c"]
    condition = answer["current"]["condition"]["text"]

    res = (
        f"{city}/{country} "
        f"{datetime_} "
        f"Weather: {temp_c} "
        f"Celsius, {condition}"
    )
    print(f"Performing request to Weather API for city {FILTER_CITY}...")
    print(res)


if __name__ == "__main__":
    get_weather()
