import os

import requests

URL = "https://api.weatherapi.com/v1/current.json?key="
FILTERING = "&q=Paris"


def get_weather() -> None:
    results = requests.get(URL + os.environ.get("API_KEY") + f"{FILTERING}")
    data = results.json()
    result = (f"{data['location']['name']}/"
              f"{data['location']['country']} "
              f"{data['location']['localtime']} "
              f"Weather: {data['current']['temp_c']} Celsius, "
              f"{data['current']['condition']['text']}")
    print(result)


if __name__ == "__main__":
    get_weather()
