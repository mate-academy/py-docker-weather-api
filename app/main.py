import os

import requests


def weather_parser(data_weather: dict) -> str:
    location_data = data_weather.get("location", {})
    current_data = data_weather.get("current", {})
    condition_data = current_data.get("condition", {})

    city_name = location_data.get("name", "name_unknown")
    country_name = location_data.get("country", "country_unknown")
    localtime = location_data.get("localtime", "localtime_unknown")
    temperature = current_data.get("temp_c", "temperature_unknown")
    condition_weather = condition_data.get("text", "condition_weather_unknown")

    return (
        f"{city_name}/{country_name} {localtime} "
        f"Weather: {temperature} Celsius, {condition_weather}"
    )


API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("Please enter value your API key")

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
PARAMS = {"q": FILTERING, "key": API_KEY}


def get_weather(url: str, params: dict) -> str:
    response = requests.get(url, params)

    if response.status_code == 200:
        data_weather = response.json()
        return weather_parser(data_weather)
    return f"Something went wrong: Error: {response.status_code}"


if __name__ == "__main__":
    print(get_weather(url=URL, params=PARAMS))
