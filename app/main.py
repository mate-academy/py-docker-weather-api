import os
import requests


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable not set.")
        return

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"HTTP request failed: {e}")
        return

    data = response.json()
    location = data["location"]["name"]
    country = data["location"]["country"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{location}, {country}: {temp}°C, {condition}")


if __name__ == "__main__":
    get_weather()
