import os
import sys
import requests

def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is not set", file=sys.stderr)
        sys.exit(1)

    url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": "Paris"}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()

    loc = data["location"]["name"]
    cond = data["current"]["condition"]["text"]
    temp_c = data["current"]["temp_c"]
    print(f"Current weather in {loc}: {cond}, {temp_c}°C")

if __name__ == "__main__":
    get_weather()
