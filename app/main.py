import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not set")
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": "Paris"
    }
    result = requests.get(url, params=params)
    data = result.json()
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    print(f"Weather in Paris: {temp_c}°C, {condition}")


if __name__ == "__main__":
    get_weather()
