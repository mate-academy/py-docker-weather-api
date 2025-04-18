import os
from dotenv import load_dotenv
import requests


def get_weather() -> None:
    load_dotenv()
    api_key = os.getenv("API_KEY", None)
    params = {
        "q": "Paris",
        "lang": "en",
        "key": api_key
    }

    try:
        response = requests.get(
            "https://api.weatherapi.com/v1/current.json",
            params=params
        )
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(e.args[0])
        return None

    city = response.json().get("location", {}).get("name")
    country = response.json().get("location", {}).get("country")
    localtime = response.json().get("location", {}).get("localtime")
    temperature = response.json().get("current", {}).get("temp_c")
    text = (response.json()
            .get("current", {}).get("condition", {}).get("text"))

    print("Performing request to Weather API for city Paris...")
    print(f"{city}/{country} {localtime} "
          f"Weather: {temperature} Celsius, {text}")


if __name__ == "__main__":
    get_weather()
