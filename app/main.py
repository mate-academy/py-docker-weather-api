import os


import requests


URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:

    response = requests.get(URL, params={"key": API_KEY, "q": CITY}).json()
    location = (
        f"{response['location']['name']}/{response['location']['country']}"
    )
    time = response["location"]["localtime"]
    weather = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]

    print("Performing request to Weather API for city Paris...")
    print(f"{location} {time} Weather: {weather} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
