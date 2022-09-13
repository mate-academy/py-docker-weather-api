import requests
import os

API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json?&q=Paris"


def get_weather():
    response = requests.get(URL,
                            params={"key": API_KEY},
                            )

    datetime = response.json()["location"]["localtime"]
    temp = response.json()["current"]["temp_c"]
    condition = response.json()["current"]["condition"]["text"]

    print(f"Paris/France {datetime} Weather: {temp} Celsium {condition}")


if __name__ == "__main__":
    get_weather()
