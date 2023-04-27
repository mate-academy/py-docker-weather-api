import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    API_KEY = os.environ.get("API_KEY")
    URL = "https://api.weatherapi.com/v1/current.json?"
    FILTERING = "Paris"

    response = requests.get(URL + f"key={API_KEY}&q={FILTERING}")

    if response.status_code == 200:
        data = response.json()
        location = data["location"]
        current = data["current"]
        city = location["name"]
        country = location["country"]
        date = current["last_updated"]
        temperature = current["temp_c"]
        condition = current["condition"]["text"]
        print(
            f"{city}/{country} {date} "
            f"Weather: {temperature} Celsius, {condition}"
        )
    else:
        print("Failed to fetch weather data")


if __name__ == "__main__":
    get_weather()
