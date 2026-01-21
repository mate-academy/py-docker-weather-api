import os
import requests

WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> tuple[float, str]:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise Exception("API_KEY environment variable is not set")

    params = {
        "key": api_key,
        "q": CITY,
    }
    response = requests.get(WEATHER_API_URL, params=params)
    if response.status_code != 200:
        raise Exception(f"Request failed {response.status_code}")
    data = response.json()

    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    return temperature, condition


if __name__ == "__main__":
    temperature, condition = get_weather()
    print(f"Paris: {temperature} °C, {condition}")
