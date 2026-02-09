import os
import requests

# Константи на рівні модуля (Module-level constants)
API_KEY = os.getenv("API_KEY")
CITY = "Paris"
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    if not API_KEY:
        print("Error: API_KEY is not set.")
        return

    # Формування фінального URL з констант
    request_url = f"{BASE_URL}?key={API_KEY}&q={CITY}"

    try:
        response = requests.get(request_url)
        response.raise_for_status()
        data = response.json()

        condition = data["current"]["condition"]["text"]
        temp = data["current"]["temp_c"]
        location = data["location"]["name"]
        country = data["location"]["country"]
        localtime = data["location"]["localtime"]

        print(f"{location}/{country} {localtime} "
              f"Weather: {temp} Celsius, {condition}")
    except requests.RequestException as e:
        print(f"Failed to get weather: {e}")


if __name__ == "__main__":
    get_weather()
