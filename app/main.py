import os
import requests


def get_weather() -> None:

    api_key = os.getenv("api_key")

    if not api_key:
        raise ValueError("api_key environment variable is required")

    BASE_URL = "http://api.weatherapi.com/v1/current.json"

    CITY = "Paris"

    url = f"{BASE_URL}?key={api_key}&q={CITY}"

    response = requests.get(url)
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
