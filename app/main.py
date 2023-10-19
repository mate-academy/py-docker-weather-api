import os
import requests

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    payload = {"q": FILTERING, "key": api_key}

    request = requests.get(URL, params=payload)
    weather_data = request.json()

    print("Performing request to Weather API for city Paris...")
    print(
        f"Paris/France {weather_data['location']['localtime']} "
        f"Weather: {weather_data['current']['temp_c']} Celsius, "
        f"{weather_data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
