import json

from dotenv import load_dotenv

import os
import requests

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
api_key = os.getenv("API_KEY")


def get_weather() -> None:
    print("Performing request to WeatherAPI for city Paris...")
    result = requests.get(
        URL,
        params={"key": api_key, "q": FILTERING}
    )
    data = json.loads(result.content)
    print(f"{data['location']['name']}/{data['location']['country']} "
          f"{data['location']['localtime']} "
          f"Weather: {data['current']['temp_c']} Celsius, "
          f"{data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
