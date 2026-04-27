import requests
import os

API_KEY = os.environ.get("API_KEY")


def get_weather() -> dict:
    response = requests.get(
        "http://api.weatherapi.com/v1/current.json",
        params={"key": API_KEY, "q": "Paris"},
    )
    data = response.json()

    location = data["location"]
    current = data["current"]
    condition = data["current"]["condition"]

    print(f"Weather in {location['name']}, {location['country']}:")
    print(f"Temperature: {current['temp_c']}")
    print(f"Actual condtion: {condition['text']}")

    return data


if __name__ == "__main__":
    get_weather()
