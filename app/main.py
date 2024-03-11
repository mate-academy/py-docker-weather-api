import os

import requests


url = "http://api.weatherapi.com/v1/current.json"
filter_city = "Paris"
api_key = os.environ.get("API_KEY")


def get_weather() -> None:
    request = requests.get(f"{url}?key={api_key}&q={filter_city}&aqi=no")
    if request.status_code == 200:
        data = request.json()
        print(f"Request to Weather API for city {filter_city}")
        print(
            f"{data["location"]["name"]}, {data["location"]["country"]} "
            f"{data["location"]["localtime"]} "
            f"Weather: {data["current"]["temp_c"]} Celsius, "
            f"{data["current"]["condition"]["text"]}"
        )
    else:
        print("Something went wrong")


if __name__ == "__main__":
    get_weather()
