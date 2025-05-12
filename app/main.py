import requests
import sys
import os


API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    if not API_KEY:
        print("Error: API_KEY environment variable is not set.")
        sys.exit(1)

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Paris"
    response = requests.get(url)

    if response.status_code == 401:
        print("Error: Invalid API key.")
        sys.exit(1)

    print(response.json())


if __name__ == "__main__":
    get_weather()
