import os
import requests

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
URL = f"{BASE_URL}?key={API_KEY}&q={CITY}"


def get_weather() -> None:

    if not API_KEY:
        raise ValueError("API_KEY environment variable is required")

    response = requests.get(URL)
    response.raise_for_status()

    data = response.json()

    city = data["location"]["name"]
    country = data["location"]["country"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"City: {city}")
    print(f"Country: {country}")
    print(f"Temperature: {temp}C")
    print(f"Condition: {condition}")


if __name__ == "__main__":
    get_weather()
