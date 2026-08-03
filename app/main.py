import os
import requests


def get_weather() -> str | None:
    api_key = os.environ.get("API_KEY")
    city = "Paris"

    if not api_key:
        print("Error: API_KEY environment variable is not set")
        return

    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        location = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Weather in {location}, {country}: ")
        print(f"Temperature: {temp_c} C")
        print(f"Condition: {condition}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
