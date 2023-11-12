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
    print(response_data)

    location_data = response_data.get("location", {})
    weather_data = response_data.get("current", {})

    country = location_data.get("country")
    city = location_data.get("name")
    localtime = location_data.get("localtime")
    temperature = weather_data.get("temp_c")
    conditions = weather_data.get("condition", {}).get("text")

    location = f"{city}/{country}"
    weather = f"Weather: {temperature} Celsius, {conditions}"

    print(f"Performing request to Weather API for city {city}...")
    print(f"{location} {localtime} {weather}")


if __name__ == "__main__":
    get_weather()
