import os
import requests

API_KEY = os.environ.get("API_KEY")
CITY = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY,
    }
    response = requests.get(URL, params=params)
    response.raise_for_status()
    data = response.json()
    location = data.get("location")
    current = data.get("current")
    condition = current.get("condition")

    result = (
        f"{location.get('name')}/{location.get('country')}\n"
        f"Temperature: {current.get('temp_c')}°C\n"
        f"Condition: {condition.get('text')}\n"
        f"Date: {current.get('last_updated')}\n"
    )
    print(result)


if __name__ == "__main__":
    get_weather()
