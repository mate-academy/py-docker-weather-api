import os

import requests


def get_weather() -> None:
    print(f"Performing request to Weather API for city Paris...")
    api_key = os.environ.get("API_KEY")
    if api_key is None:
        raise Exception("API Key not found.")
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris"
    response = requests.get(url)
    if response.status_code == 200:
        retrieve_result(response)
    else:
        raise Exception("Bad request. Check API key and WeatherAPI status")


def retrieve_result(input):
    data = input.json()
    print(
        f"{data['location']['name']}/{data['location']['country']} "
        f"{data['location']['localtime']} "
        f"Weather: {data['current']['temp_c']} Celsius, "
        f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
