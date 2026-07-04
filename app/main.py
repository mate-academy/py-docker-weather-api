import os
import requests

API_KEY = os.environ["API_KEY"]
URL = "http://api.weatherapi.com/v1/current.json?key=" + API_KEY
FILTERING = "Paris"


def get_weather() -> None:
    print(f"Performinng request to Weather API for city {FILTERING}...")

    response = requests.get(URL + f"&q={FILTERING}")
    result = response.json()
    formatted_result = f"{result['location']['name']}/" \
        f"{result['location']['country']} " \
        f"{result['location']['localtime']} Weather: " \
        f"{result['current']['temp_c']} Celsius," \
        f"{result['current']['condition']['text']}"

    print(formatted_result)


if __name__ == "__main__":
    get_weather()
