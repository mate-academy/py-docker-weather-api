import requests
import os

URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    result = requests.get(
        URL
        + "?"
        + f"key={API_KEY}"
        + "&"
        + f"q={FILTERING}"
        + "&"
        + "aqi=no"
    )

    print("Performing request to Weather API for city Paris...")
    print(
        f"{result.json()['location']['name']}/"
        f"{result.json()['location']['country']} "
        f"{result.json()['location']['localtime']} "
        f"Weather: {result.json()['current']['temp_c']} Celsius, "
        f"{result.json()['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
