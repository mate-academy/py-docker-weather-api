import os
import requests

URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    print(f"Performing request to Weather API for city {FILTERING}...")
    result = requests.get(URL, params={"key": API_KEY, "q": FILTERING})
    if result.status_code == requests.codes.ok:
        data = result.json()
        city = data.get("location").get("name")
        country = data.get("location").get("country")
        location = f"{city}/{country}"
        date = data.get("location").get("localtime")
        temperature = data.get("current").get("temp_c")
        condition = data.get("current").get("condition").get("text")
        print(f"{location} {date} Weather: {temperature} Celsius, {condition}")
    else:
        print("Something goes wrong, check your connection")


if __name__ == "__main__":
    get_weather()
