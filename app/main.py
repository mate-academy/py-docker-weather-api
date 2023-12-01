import os
import requests


URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": FILTERING
    }
    result = requests.get(URL, params=params).json()

    print(
        "Performing request to Weather API "
        f"for city {result['location']['name']}...\n"
        f"{result['location']['name']}/{result['location']['country']} "
        f"{result['current']['last_updated']} Weather: "
        f"{result['current']['temp_c']} Celsius, "
        f"{result['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
