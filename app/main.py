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

    # Перевірка наявності ключів
    if "location" not in data or "current" not in data:
        print(f"Error: Unexpected API response structure: {data}")
        return

    location = data["location"].get("name")
    country = data["location"].get("country")
    current = data["current"]
    temp = current.get("temp_c")
    condition = current.get("condition", {}).get("text")

    if None in (location, country, temp, condition):
        print(f"Error: Missing weather data in API response: {data}")
        return

    print(f"{location}, {country}: {temp}°C, {condition}")


if __name__ == "__main__":
    get_weather()
