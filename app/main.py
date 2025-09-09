import os
import requests


URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY is not set")

    url = f"{URL}?key={api_key}&q={CITY}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    localtime = data["location"]["localtime"]
    country = data["location"]["country"]
    location = data["location"]["name"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{location}/{country}"
          f" {localtime} Weather: "
          f"{temp_c} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
