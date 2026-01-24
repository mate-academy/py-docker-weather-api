import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise RuntimeError("API_KEY environment variable is not set")

    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": "Paris",
        "aqi": "no",
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    location = data["location"]["name"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"City: {location}")
    print(f"Temperature: {temp_c}°C")
    print(f"Condition: {condition}")


if __name__ == "__main__":
    get_weather()
