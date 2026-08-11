import os

import requests


API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> dict:
    api_key = os.environ["API_KEY"]

    response = requests.get(
        API_URL,
        params={
            "key": api_key,
            "q": CITY,
        },
        timeout=10,
    )

    response.raise_for_status()

    return response.json()


def main() -> None:
    weather = get_weather()

    city = weather["location"]["name"]
    temperature = weather["current"]["temp_c"]
    condition = weather["current"]["condition"]["text"]

    print(f"{city}: {temperature}°C, {condition}")


if __name__ == "__main__":
    main()
