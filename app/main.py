import os
import sys
import requests


URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)
    params = {
        "key": api_key,
        "q": CITY
    }
    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        data = response.json()
        location = data["location"]["name"]
        condition = data["current"]["condition"]["text"]
        temp_c = data["current"]["temp_c"]
        print(f"Weather in {location}: {condition}, {temp_c}°C")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Weather API: {e}", file=sys.stderr)
        sys.exit(1)
if __name__ == "__main__":
    get_weather()
