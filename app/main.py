import os
import sys
import requests
from requests.exceptions import RequestException
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    print("Missing API_KEY environment variable")
    sys.exit(1)

CITY = "Paris"
API_BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    try:
        response = requests.get(
            API_BASE_URL,
            params={"key": API_KEY, "q": CITY}
        )
        response.raise_for_status()
        res = response.json()
    except RequestException as e:
        print(f"Network error: {e}")
        sys.exit(1)
    except ValueError:
        print("Failed to parse JSON response")
        sys.exit(1)

    location = res.get('location', {})
    current = res.get('current', {})
    condition = current.get('condition', {})

    print(
        f"City: {location.get('name', 'N/A')}\n"
        f"Weather: {condition.get('text', 'N/A')}\n"
        f"Temperature: {current.get('temp_c', 'N/A')}\n"
        f"Feels like: {current.get('feelslike_c', 'N/A')}\n"
        f"Wind: {current.get('wind_kph', 'N/A')}\n"
        f"Clouds: {current.get('cloud', 'N/A')}\n"
        f"Heat index: {current.get('heatindex_c', 'N/A')}"
    )


if __name__ == "__main__":
    get_weather()
