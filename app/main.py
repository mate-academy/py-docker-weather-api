import requests
import os


KEY = os.environ["API_KEY"]
CITY = "Paris"
URL = f"https://api.weatherapi.com/v1/current.json?key={KEY}&q={CITY}"


def get_weather():
    response_json = requests.get(URL).json()
    location = f"{response_json['location']['name']}/{response_json['location']['country']}"
    local_time = response_json['location']["localtime"]

    weather = f"Weather: {response_json['current']['temp_c']} Celsius," \
              f" {response_json['current']['condition']['text']}"

    print(f"{location} {local_time} {weather}")
    return response_json


if __name__ == "__main__":
    get_weather()
