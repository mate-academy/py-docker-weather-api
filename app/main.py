import os

import requests


API_KEY = os.environ.get("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json?"
FILTER = "Kiev"


def get_weather() -> None:
    if not API_KEY:
        raise SystemExit("API_KEY not found.")

    try:
        response = requests.get(url=URL, params={"key": API_KEY, "q": FILTER})
        response.raise_for_status()
    except requests.exceptions.RequestException as exception:
        raise SystemExit(exception)

    data = response.json()

    print(
        f"The weather in {data['location']['name']} "
        f"{data['location']['country']}:\n"
        f"{data['location']['localtime']}\n"
        f"Weather: {data['current']['temp_c']} Celsius,\n"
        f"{data['current']['condition']['text']}\n"
        f"Wind: {data['current']['wind_kph']} km/h\n"

    )


if __name__ == "__main__":
    get_weather()
