import os
import requests
from dotenv import load_dotenv


URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    load_dotenv()
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        print("Error: WEATHER_API_KEY environment variable is not set")
        return

    payload = {"key": api_key, "q": FILTERING, "aqi": "no"}
    response = requests.get(URL, params=payload)
    if response.status_code == 200:
        data = response.json()
        if not data["location"] or not data["current"]:
            print("Error: Incomplete data received from API.")
            return
        location = data["location"]
        current_data = data["current"]
        temp = current_data["temp_c"]
        current_weather = (
            f'{location["name"]}/{location["country"]} '
            f'{location["localtime"]} Weather: {temp} Celsius, '
            f'{current_data["condition"]["text"]}'
        )
        print(current_weather)

    else:
        print(f"Error: Failed to fetch data from Weather API. "
              f"Status code: {response.status_code}")
        return


if __name__ == "__main__":
    get_weather()
