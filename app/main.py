import os

import requests

API_KEY = os.environ.get("API_KEY")
CITY = "Paris"
URL = f"http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")
    if API_KEY is None:
        raise Exception("API Key not found.")
    url = URL + f"?key={API_KEY}&q={CITY}"
    response = requests.get(url)
    if response.status_code == 200:
        retrieve_result(response)
    else:
        raise Exception(response.status_code)


def retrieve_result(input_response: requests.Response) -> None:
    data = input_response.json()
    location = data["location"]
    current = data["current"]
    print(
        f"{location['name']}/{location['country']} "
        f"{location['localtime']} "
        f"Weather: {current['temp_c']} Celsius, "
        f"{current['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
