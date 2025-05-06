import os

import requests

API_KEY = ""
CITY = "Paris"

def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found in environment variables.")

    url = f"http://api.weatherapi.com/v1/current.json?q={CITY}&key={api_key}"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    city = data['location']['name']
    temp_c = data['current']['temp_c']
    condition = data['current']['condition']['text']

    print(f"Weather in {city}: {temp_c}°C, {condition}")


if __name__ == "__main__":
    get_weather()
