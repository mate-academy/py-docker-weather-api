import os
import requests
from dotenv import load_dotenv


load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:

    if not API_KEY:
        print("API_KEY is missing or empty. "
              "Please set the environment variable.")
        return

    params = {
        "key": API_KEY,
        "q": FILTERING
    }

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        data = response.json()

        location = data.get("location", {})
        current = data.get("current", {})

        if not location or not current:
            print("Error: Missing required data in API response.")
            return

        country = location.get("country", "Unknown")
        localtime = location.get("localtime", "Unknown time")
        temperature = current.get("temp_c", "N/A")
        condition = current.get("condition", {}).get("text", "N/A")

        print(f"Performing request to Weather API for city {FILTERING}...")
        print(f"{FILTERING}/{country} - {localtime}")
        print(f"Temperature: {temperature}°C, Condition: {condition}")

    except requests.exceptions.RequestException as e:
        print(f" Network/API error: {e}")
    except KeyError as e:
        print(f" Error: Missing key in response - {e}")
    except Exception as e:
        print(f" Unexpected error: {e}")


if __name__ == "__main__":
    get_weather()
