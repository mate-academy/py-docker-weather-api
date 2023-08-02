import requests
import os

URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    result = requests.get(
        URL
        + f"{URL}?key={API_KEY}&q={FILTERING}&aqi=no"
    ).json()

    print("Performing request to Weather API for city Paris...")
    print(
        f"{result['location']['name']}/"
        f"{result['location']['country']} "
        f"{result['location']['localtime']} "
        f"Weather: {result['current']['temp_c']} Celsius, "
        f"{result['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
