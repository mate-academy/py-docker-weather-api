import os

import requests

FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={FILTERING}"


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        print(
            f"{data['location']['name']}/{data['location']['country']} "
            f"{data['location']['localtime']} "
            f"Weather: {data['current']['temp_c']} Celsius, "
            f"{data['current']['condition']['text']}"
        )
    else:
        print("Failed to fetch weather data.")


if __name__ == "__main__":
    get_weather()
