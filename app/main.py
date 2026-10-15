import os
import requests


CITY = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")


def get_weather() -> dict:
    if not API_KEY:
        raise ValueError(
            "API_KEY environment variable is not set."
        )
    params = {
        "q": CITY,
        "key": API_KEY,
    }
    response = requests.get(URL, params=params)
    response.raise_for_status()
    return response.json()


def main() -> None:
    weather = get_weather()
    location = weather["location"]
    current = weather["current"]
    print(
        f"{location['name']}/{location['country']} "
        f"{location['localtime']} "
        f"Weather: {current['temp_c']} Celsius, "
        f"{current['condition']['text']}"
    )


if __name__ == "__main__":
    main()
