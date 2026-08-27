import os
import requests

URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")

    if not api_key:
        print("API_KEY is missing!")
        return

    result = requests.get(URL + f"key={api_key}&q={FILTERING}")

    if result.status_code == 200:
        data = result.json()
        print(f"Weather in {FILTERING}: {data['current']['temp_c']}°C")
    else:
        print(f"Failed to fetch data. Status code: {result.status_code}")


if __name__ == "__main__":
    get_weather()
