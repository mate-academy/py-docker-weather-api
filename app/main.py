import os
import sys
import requests

URL = "https://api.weatherapi.com/v1/current.json?"
FILTER = "Paris"

API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:

    if not API_KEY:
        print("Error: API_KEY environment variable not set!")
        sys.exit(1)
    response = requests.get(URL + f"key={API_KEY}&q={FILTER}")
    if response.status_code == 200:
        data = response.json()
        location = f"{data['location']['name']}/{data['location']['country']}"
        localtime = data['location']['localtime']
        temp = f"{data['current']['temp_c']}°C"
        condition = data['current']['condition']['text']

        print(f"{location} {localtime} Weather: {temp}, {condition}")

    else:
        print("Error:", response.status_code, response.text)


if __name__ == "__main__":
    get_weather()
