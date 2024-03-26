import os

import requests

API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")
    response = requests.get(URL,
                            params={"key": API_KEY, "q": FILTERING})

    if response.status_code != requests.codes.ok:
        print(f"Request failed. Status code: {response.status_code}. "
              f"Message: {response.text}")
        return
    data = response.json()
    print(f"{data['location']['name']}/{data['location']['country']} "
          f"{data['location']['localtime']} "
          f"Weather: {data['current']['temp_c']} Celsius, "
          f"{data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
