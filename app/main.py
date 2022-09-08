import requests
import os

API_Key = "87b89b1e34ef4ac3aa4143849220809"


def get_weather():
    response = requests.get(
        "http://api.weatherapi.com/v1/current.json?&q=Paris",
        params={"key": os.environ.get("API_KEY")},
    )

    datetime = response.json()["location"]["localtime"]
    temp = response.json()["current"]["temp_c"]
    condition = response.json()["current"]["condition"]["text"]

    print(f"Paris/France {datetime} Weather: {temp} Celsium {condition}")

    # print(response.text)


if __name__ == "__main__":
    get_weather()
