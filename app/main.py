import os
import requests


CITY = "Paris"
KEY = os.environ["API_KEY"]
URL = f"https://api.weatherapi.com/v1/current.json?q={CITY}"


def get_weather() -> None:
    key_value = {
        "key": KEY,
    }

    result = requests.get(URL, headers=key_value)

    data_value = result.json()
    country = data_value["location"]["country"]
    last_data = data_value["current"]["last_updated"]
    temperature = data_value["current"]["temp_c"]
    weather = data_value["current"]["condition"]["text"]
    result_string = (f"{CITY}/{country} {last_data} "
                     f"Weather: {temperature} Celsius, {weather}")
    print(f"Performing request to Weather API for city {CITY}...")
    print(result_string)


if __name__ == "__main__":
    get_weather()
