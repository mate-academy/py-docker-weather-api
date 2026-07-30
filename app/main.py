import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    response = requests.get(
        url="https://api.weatherapi.com/v1/current.json",
        params={
            "key": api_key,
            "q": "Paris",
        }
    )
    weather = response.json()
    print(weather["location"]["name"])
    print(weather["current"]["temp_c"])
    print(weather["current"]["condition"]["text"])


if __name__ == "__main__":
    get_weather()
