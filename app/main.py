import os

import requests

URL = "http://api.weatherapi.com/v1/current.json?"
CITY = "PARIS"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(URL + f"key={API_KEY}&q={CITY}").json()

    city = response["location"]["name"]
    country = response["location"]["country"]
    temperature = response["current"]["temp_c"]
    conditions = response["current"]["condition"]["text"]

    print(f"Performing request to Weather API for {city}...")
    print(
        f"For {city} in {country} "
        f"the temperature is {temperature}°C and the conditions are {conditions}."
    )


if __name__ == "__main__":
    get_weather()
