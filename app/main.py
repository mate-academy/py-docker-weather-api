import requests
import os


BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    if not API_KEY:
        print("Error: API_KEY environment variable is not set.")
        return

    try:
        response = requests.get(BASE_URL, params={"key": API_KEY, "q": CITY})
        response.raise_for_status()
        data = response.json()

        print(f'Current weather in {data["location"]["name"]}: ')
        print(f'Temperature: {data["current"]["temp_c"]}°C')
        print(f'Condition: {data["current"]["condition"]["text"]}')

    except Exception as err:
        print(f"An error occurred: {err}")


if __name__ == "__main__":
    get_weather()
