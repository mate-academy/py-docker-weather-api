import os

import requests


url = "http://api.weatherapi.com/v1/current.json"
filter_city = "Paris"
api_key = os.environ.get("API_KEY")


def get_weather() -> None:

    response = requests.get(f"{url}?key={api_key}&q={filter_city}&aqi=no")

    if response.status_code == 200:
        data = response.json()
        print(f"City: {data['location']['name']}/"
              f"{data['location']['country']}")
        print(f"Local Time: {data['location']['localtime']}")
        print(f"Weather: {data['current']['temp_c']} Celsius, "
              f"{data['current']['condition']['text']}")
    else:
        print(f"Error: {response.status_code}. "
              f"Something went wrong with the Weather API request.")


if __name__ == "__main__":
    get_weather()
