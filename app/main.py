import os

from dotenv import load_dotenv
import requests


load_dotenv()


API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/"
FILTERING = "Paris"


def get_weather() -> None:
    result = requests.get(
        URL + "current.json", params={"key": API_KEY, "q": FILTERING}
    )

    data = result.json()
    location = data.get("location", {}).get("name", "Unknown location")
    temp_c = data.get("current", {}).get("temp_c", "N/A")
    condition = data.get("current", {}).get("condition", {}).get("text", "N/A")
    print(f"Weather in {location}: {temp_c}°C, {condition}")


if __name__ == "__main__":
    get_weather()
