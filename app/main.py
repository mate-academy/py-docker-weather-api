import os
import requests

from dotenv import load_dotenv


load_dotenv()

BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_url() -> str:
    api_key = os.getenv("API_KEY")
    return f"{BASE_URL}?key={api_key}&q=Paris"


def get_weather() -> None:
    url = get_url()

    response = requests.get(url)

    data = response.json()
    location = data.get("location")
    city = location.get("name")
    country = location.get("country")
    current = data.get("current")
    last_updated = current.get("last_updated")
    temp_c = current.get("temp_c")
    condition = current.get("condition").get("text")

    print("Performing request to Weather API for city Paris")
    print(f"{city}/{country} {last_updated}", end="")
    print(f"Weather: {temp_c} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
