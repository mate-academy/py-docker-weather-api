import os
import requests

API_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is missing!")
        return

    url = f"{API_URL}?q={CITY}&key={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["current"]["temp_c"]
            desc = data["current"]["condition"]["text"]
            print(f"Weather in {CITY}: {temp}°C, {desc}")
        else:
            msg = data.get("message", "Unknown error")
            print(f"Failed to fetch weather: {msg}")

    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    get_weather()
