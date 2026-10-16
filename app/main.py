import os
import requests


URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("API_KEY not set")
        return

    print(f"Performing request to Weather API for city {CITY}...")
    response = requests.get(URL, params={"key": api_key, "q": CITY})
    response.raise_for_status()
    data = response.json()

    location = data["location"]
    current = data["current"]

    city_name = location["name"]
    country = location["country"]
    local_time = location["localtime"]
    temperature = current["temp_c"]
    condition = current["condition"]["text"]

    print(
        f"{city_name}/{country} {local_time} "
        f"Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
