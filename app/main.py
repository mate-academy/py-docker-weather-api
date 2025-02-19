import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": FILTERING
    }

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()

        data = response.json()

        current_weather = data.get("current")
        location = data.get("location")

        temp_c = current_weather.get("temp_c")
        last_updated = current_weather.get("last_updated")
        weather_condition = current_weather.get("condition").get("text")

        city = location.get("name")
        country = location.get("country")

        print(f"Performing request to Weather API for city {city}...")
        print(
            f"{city}/{country} {last_updated} Weather: "
            f"{temp_c} Celsius, {weather_condition}"
        )
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    get_weather()
