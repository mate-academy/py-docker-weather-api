import os
import requests


URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(url=URL, params={"key": API_KEY, "q": CITY})
    print("Performing request to Weather API for city Paris...")
    if response.status_code == 200:
        response_json = response.json()
        print(f"{response_json['location']['name']}"
              f"/{response_json['location']['country']}"
              f" {response_json['location']['localtime']}"
              f" Weather: {response_json['current']['temp_c']} Celsius,"
              f" {response_json['current']['condition']['text']}")
    else:
        print("An error occurred, try again later!")


if __name__ == "__main__":
    get_weather()
