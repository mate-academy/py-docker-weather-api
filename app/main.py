import os

import requests

API_KEY = os.getenv("API_KEY")

URL = "https://api.weatherapi.com/v1/current.json"

def get_weather(city: str) -> None:
    if not API_KEY:
        raise RuntimeError("API_KEY environment variable is not set.")

    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "no",
    }

    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    print(f"City: {data['location']['name']}")
    print(f"Country: {data['location']['country']}")
    print(f"Temperature: {data['current']['temp_c']}°C")
    print(f"Weather: {data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather("Paris")
