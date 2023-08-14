import requests
import os


URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    print(f"Performing request to Weather API for city {FILTERING}...")
    result = (requests.get(URL + f"q={FILTERING}&key={API_KEY}")).json()
    if result.get("error"):
        print(f"{result.get('error').get('message', 'oops, something wrong')}")
        return
    print(f"{result['location']['tz_id']} "
          f"{result['current']['last_updated']} "
          f"Weather: {result['current']['temp_c']} Celsius",
          f"{result['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
