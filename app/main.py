import os
import requests

CITY = "Paris"
WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")

    if not api_key:
        print("API key not set")
        return

    params = {
        "key": api_key,
        "q": CITY
    }

    response = requests.get(WEATHER_API_URL, params=params)
    response.raise_for_status()

    data = response.json()

    print(f"City: {data['location']['name']}")
    print(f"Country: {data['location']['country']}")
    print(f"Temperature: {data['current']['temp_c']}°C")
    print(f"Condition: {data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
