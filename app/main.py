import requests
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY", None)


def get_weather() -> None:
    if API_KEY is None:
        print("Error: API_KEY is not set or empty.")
        return

    print("Performing Weather API request...")

    params = {
        "key": API_KEY,
        "q": FILTERING,
    }

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        data = response.json()

        location = data.get("location", {})
        current = data.get("current", {})

        if not location or not current:
            print("Error: Data is missing or empty in response.")
            return

        country = location.get("country", "N/A")
        localtime = location.get("localtime", "N/A")
        temp = current.get("temp_c", "N/A")
        condition = current.get("condition", {}).get("text", "N/A")

        print(f"{FILTERING}({country}) {localtime}")
        print(f"{temp}°C, {condition}")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_weather()
