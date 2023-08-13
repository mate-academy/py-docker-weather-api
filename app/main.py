import requests
import json
import os


URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    result = requests.get(URL + f"q={FILTERING}&key={API_KEY}")
    result = json.loads(result.content)
    if result.get("error"):
        print(f"{result.get('error').get('message')}")
        return
    print(f"{result.get('location').get('tz_id')} "
          f"{result.get('current').get('last_updated')} "
          f"Weather: {result.get('current').get('temp_c')} Celsius",
          f"{result.get('current').get('condition').get('text')}")


if __name__ == "__main__":
    get_weather()
