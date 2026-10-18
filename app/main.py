import requests
import os


BASE_URL = "http://api.weatherapi.com/v1/current.json?key="
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:

    if not API_KEY:
        raise ValueError("API_KEY environment variable is not set")

    request = requests.get(f"{BASE_URL}{API_KEY}&q={FILTERING}")

    print(request.text)


if __name__ == "__main__":
    get_weather()
