import os
import requests
import json

from typing import Union


def get_weather(api_key: str, city: str = "Paris") -> Union[dict, str]:
    url = f"http://api.weatherapi.com/v1/current.json?q={city}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    return json.dumps(data, indent=2)


if __name__ == "__main__":
    api_key = os.environ.get("WEATHER_API_KEY")

    if not api_key:
        raise ValueError("WEATHER_API_KEY environment variable is not set.")

    weather_data = get_weather(api_key)
    print(f"Weather in Paris: {weather_data}")
