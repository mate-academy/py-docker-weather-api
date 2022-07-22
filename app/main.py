import os
import requests


GLOBAL_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather():
    """
    default ['API_KEY'] = '828f09aa85dc4173bc0103345222107'
    """
    key = os.getenv("API_KEY", None)
    city = "Paris"

    if not key:
        print("Ypu need to use 'API_KEY'")
        return

    params = {
        "key": key,
        "q": city
    }

    request = requests.get(url=GLOBAL_URL, params=params)

    data = request.json()

    country = data["location"]["country"]
    local_time = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Location: {city}/{country},\n"
          f"local time: {local_time},\n"
          f"Weather: {temperature} °C, {condition}")


if __name__ == "__main__":
    get_weather()
