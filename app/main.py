import os
import requests

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is missing.")
        return

    request_url = f"{URL}?key={api_key}&q={CITY}"

    try:
        response = requests.get(request_url)
        response.raise_for_status()
        data = response.json()

        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Current weather in Paris: {temp} °C, {condition}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to get weather data: {e}")


if __name__ == "__main__":
    get_weather()
