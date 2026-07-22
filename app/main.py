import os
import sys
import requests

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        sys.exit("Error: API_KEY environment variable is missing.")

    params = {"key": api_key, "q": CITY}

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        data = response.json()

        location = data["location"]["name"]
        country = data["location"]["country"]
        local_time = data["location"]["localtime"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Performing request to Weather API for city {CITY}...")
        output = (
            f"{location}/{country} {local_time} "
            f"Weather: {temp_c} Celsius, {condition}"
        )
        print(output)

    except requests.exceptions.RequestException as error:
        sys.exit(f"Error fetching weather data: {error}")


if __name__ == "__main__":
    get_weather()
