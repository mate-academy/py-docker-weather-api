import requests
import os


BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
WEATHERAPI_KEY = os.getenv("WEATHERAPI_KEY")


def get_weather() -> None:
    if not WEATHERAPI_KEY:
        print("Error: API_KEY is not set.")
        return

    print(f"Performing request to Weather API for city {CITY}...")

    try:
        response = requests.get(
            BASE_URL,
            params={"key": WEATHERAPI_KEY, "q": CITY}
        )
        response.raise_for_status()
        weather_data = response.json()

        print(
            f'{weather_data["location"]["tz_id"]} '
            f'{weather_data["location"]["localtime"]} '
            f'Weather: {weather_data["current"]["temp_c"]} Celsius, '
            f'{weather_data["current"]["condition"]["text"]}'
        )
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_weather()
