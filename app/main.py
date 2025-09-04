import os

import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found in environment variables")

    city = "Paris"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    data = response.json()

    location = data["location"]["name"]
    country = data["location"]["country"]
    time = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{location}/{country} {time} "
          f"Weather: {temp_c} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
