import os
import requests


URL = "http://api.weatherapi.com/v1/current.json"
KEY = os.environ.get("API_KEY")
CITY = "Paris"


def get_weather() -> None:

    print(f"Performing request to Weather API for city {CITY}...")

    response = requests.get(URL, params={"KEY": KEY, "q": CITY}).json()

    print(
        f"{response['location']['name']}/{response['location']['country']} "
        f"{response['location']['localtime']} "
        f"Weather: {response['current']['temp_c']} Celsius, "
        f"{response['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
