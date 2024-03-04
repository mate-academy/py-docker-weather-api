import requests
import os
import json


def get_weather() -> None:
    # write your code here

    api_key = os.environ.get("API_KEY")

    url = (f"http://api.weatherapi.com/v1/current."
           f"json?key={api_key}&q=Paris")

    response = requests.get(url)

    data = response.json()

    print(data)

    print("Have a nice day!")


if __name__ == "__main__":
    get_weather()
