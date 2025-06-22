import os
import requests


URL = "https://api.weatherapi.com/v1/current.json?"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not set in environment variables")

    url = f"{URL}key={api_key}&q={CITY}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(
            f"Failed to get data from API, status code:"
            f" {response.status_code}")

    data = response.json()

    city = data["location"]["name"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"The weather in {city}: {temp}°C, {condition}")


if __name__ == "__main__":
    get_weather()
