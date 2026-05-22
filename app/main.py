import os
import requests


URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("Missing API_KEY environment variable")

    params = {
        "key": api_key,
        "q": FILTERING,
    }

    try:
        result = requests.get(URL, params=params, timeout=5)

        result.raise_for_status()

        data = result.json()

        city = data["location"]["name"]
        country = data["location"]["country"]
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Weather for {city}, {country}")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {condition}")

    except requests.Timeout:
        print("Error: request timed out")

    except requests.RequestException as e:
        print(f"Error: request failed -> {e}")


if __name__ == "__main__":
    get_weather()