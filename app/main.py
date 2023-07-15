import os
import requests


API_KEY = os.environ.get("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json?"
FILTER = "Paris"


def get_weather() -> None:
    if not API_KEY:
        raise SystemExit("API_KEY environment variable was not found.")

    print(f"Performing request to Weather API for city {FILTER}...")
    try:
        response = requests.get(url=URL, params={"key": API_KEY, "q": FILTER})
        response.raise_for_status()
    except requests.exceptions.RequestException as exception:
        raise SystemExit(exception)

    data = response.json()

    print(
        f"{data['location']['name']}/"
        f"{data['location']['country']} "
        f"{data['location']['localtime']} "
        f"Weather: {data['current']['temp_c']} Celsius, "
        f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
