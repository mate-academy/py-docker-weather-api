import os
import requests


def get_weather() -> None:

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable not set.")

    url = f"http://api.weatherapi.com/v1/current.json?q=Paris&key={api_key}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        location = data["location"]["name"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"Current weather in {location}: {temp_c}°C, {condition}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except KeyError:
        print("Unexpected response format")


if __name__ == "__main__":
    get_weather()
