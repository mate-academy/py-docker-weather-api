import os

import requests


def get_weather() -> None:
    base_url = "http://api.weatherapi.com/v1/current.json"
    key = os.getenv("API_KEY")
    city = "Paris"

    url = f"{base_url}?key={key}&q={city}"
    response = requests.get(url).json()
    print(f"Performing request to Weather API for city {city}...")
    print(
        f"{response['location']['name']}/{response['location']['country']} "
        f"{response['location']['localtime']} "
        f"Weather: {response['current']['temp_c']} Celsius, {response['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
