import os
import requests

CITY = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")

    if not api_key:
        print("API_KEY environment variable is not set")
        return

    url = f"{URL}?key={api_key}&q={CITY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        location = data["location"]
        current = data["current"]

        country = location["country"]
        localtime = location["localtime"]
        temp_c = current["temp_c"]
        condition = current["condition"]["text"]

        print(
            f"{CITY}/{country} {localtime} "
            f"Weather: {temp_c} Celsius {condition}"
        )
    else:
        print(
            f"Failed to fetch weather data. "
            f"Status code: {response.status_code}"
        )


if __name__ == "__main__":
    get_weather()
