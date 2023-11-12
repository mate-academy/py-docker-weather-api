import requests
import os


KEY = os.environ.get("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/"
FORMAT = "current.json"
FILTERING = "Paris"
AQI = "no"


def get_weather() -> None:
    payload = {"key": KEY, "q": FILTERING, "aqi": AQI}
    url = BASE_URL + FORMAT

    response = requests.get(url, params=payload)

    response_data = response.json()

    country = response_data["location"]["country"]
    city = response_data["location"]["name"]
    localtime = response_data["location"]["localtime"]
    temperature = response_data["current"]["temp_c"]
    conditions = response_data["current"]["condition"]["text"]

    location = f"{city}/{country}"
    weather = f"Weather: {temperature} Celsius, {conditions}"

    print(f"Performing request to Weather API for city {city}...")
    print(f"{location} {localtime} {weather}")


if __name__ == "__main__":
    get_weather()
