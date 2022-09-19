import requests
import os


def get_weather():
    key = os.environ["API_KEY"]
    city = "Paris"
    url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={city}"
    response_json = requests.get(url).json()
    location = f"{response_json['location']['name']}/{response_json['location']['country']}"
    local_time = response_json['location']["localtime"]
    weather = f"Weather: {response_json['current']['temp_c']} Celsius," \
              f" {response_json['current']['condition']['text']}"
    print(f"{location} {local_time} {weather}")
    return response_json


if __name__ == "__main__":
    get_weather()
