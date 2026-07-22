import os
import sys
import requests


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")

    if not api_key:
        print("API_KEY not set")
        sys.exit(1)

    city = "Paris"
    url = (
        f"http://api.weatherapi.com/v1/current.json"
        f"?key={api_key}&q={city}"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        location = data["location"]
        current = data["current"]

        print("Performing request to WEATHER API for city Paris")
        print(
            f"{location['name']}/{location['country']} "
            f"{location['localtime']} "
            f"Weather: {current['temp_c']} "
            f"Celsius, {current['condition']['text']}"
        )

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_weather()
