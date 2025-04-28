import os
import requests


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found.")

    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": "Paris",
        "aqi": "no"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    city = data["location"]["name"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Current weather in {city}: {temperature}°C, {condition}")


if __name__ == "__main__":
    get_weather()
