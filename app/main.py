import os

import requests


URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"

KEY = os.getenv("API_KEY")


def get_weather() -> None:
    if not KEY:
        raise Exception("Weather API key not found!")
    result = requests.get(URL + f"q={FILTERING}&key={KEY}")
    data = result.json()
    print(
        f"{data['location']['name']}/{data['location']['country']} "
        f"{data['location']['localtime']}\n"
        f"Weather: {data['current']['temp_c']}°C, "
        + data["current"]["condition"]["text"]
    )


if __name__ == "__main__":
    get_weather()
