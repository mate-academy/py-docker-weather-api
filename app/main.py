import os
import requests

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
AQI = "no"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise RuntimeError("API_KEY environment variable is not set")

    params = {
        "key": api_key,
        "q": CITY,
        "aqi": AQI,
    }

    response = requests.get(URL, params=params)
    response.raise_for_status()

    data = response.json()

    print(f"City: {data['location']['name']}, {data['location']['country']}")
    print(f"Temperature: {data['current']['temp_c']}°C")
    print(f"Condition: {data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
