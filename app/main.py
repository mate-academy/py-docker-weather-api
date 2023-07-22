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
        f"The weather in {data['location'].get('name', 'no value')} "
        f"{data['location'].get('country', 'no value')}:\n"
        f"{data['location'].get('localtime', 'no value')}\n"
        f"Weather: {data['current'].get('temp_c', 'no value')} Celsius,\n"
        f"{data['current'].get('condition', {}).get('text', 'no value')}\n"
        f"Wind: {data['current'].get('wind_kph', 'no value')} km/h\n"
    )


if __name__ == "__main__":
    get_weather()
