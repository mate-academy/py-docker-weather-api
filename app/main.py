import os
import requests

CITY = "Paris"
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API_KEY environment variable is not set.")
        return

    url = f"{BASE_URL}?key={api_key}&q={CITY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temp = data["current"]["temp_c"]
        cond = data["current"]["condition"]["text"]

        print(f"{CITY} Weather: {temp} Celsius, {cond}")
    except requests.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_weather()
