import os
import requests


URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    if not API_KEY:
        print("Error: API_KEY environment variable is missing.")
        return

    print(f"Performing request to Weather API for city {CITY}...")

    params = {
        "key": API_KEY,
        "q": CITY
    }

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        data = response.json()

        location = data["location"]["name"]
        country = data["location"]["country"]
        local_time = data["location"]["localtime"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(
            f"{location}/{country} {local_time} "
            f"Weather: {temp_c} Celsius, {condition}"
        )

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    get_weather()
