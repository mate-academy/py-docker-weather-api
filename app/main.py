import os
import requests
from dotenv import load_dotenv
load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"
KEY = os.getenv("API_KEY")
FILTERING = "Paris"


def get_weather() -> None:
    api_result = requests.get(
        URL,
        params=[("key", KEY), ("q", FILTERING)]
    )
    api_response = api_result.json()
    print(f"Performing request to Weather API for city {FILTERING}...")
    print(f"{api_response['location']['name']}/"
          f"{api_response['location']['country']} "
          f"{api_response['location']['localtime']} "
          f"Weather: {api_response['current']['temp_c']} Celsius, "
          f"{api_response['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
