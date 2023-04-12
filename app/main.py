import os
import requests


URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:

    key = os.environ.get("API_KEY")
    city = "Paris"

    print(f"Performing request to Weather API for city {city}...")

    response = requests.get(URL, params={"key": key, "q": city}).json()

    print(
        f"{response['location']['name']}/{response['location']['country']} "
        f"{response['location']['localtime']} "
        f"Weather: {response['current']['temp_c']} Celsius, "
        f"{response['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
