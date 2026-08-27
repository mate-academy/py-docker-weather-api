import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    url = "http://api.weatherapi.com/v1/current.json"

    response = requests.get(url, params={"key": api_key, "q": "Paris"})
    data = response.json()

    city = data["location"]["name"]
    country = data["location"]["country"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Current weather in city:"
          f" {city}, {country}, is {temp_c}°C, {condition}")


if __name__ == "__main__":
    get_weather()
