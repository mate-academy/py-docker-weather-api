import os
import requests


def get_weather():
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is missing.")
        return

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Current weather in Paris: {temp} °C, {condition}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to get weather data: {e}")


if __name__ == "__main__":
    get_weather()
