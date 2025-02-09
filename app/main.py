import os
import requests

import dotenv


dotenv.load_dotenv()


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": "Paris",
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        city = data["location"]["name"]
        country = data["location"]["country"]
        time = data["location"]["localtime"]
        temp = data["current"]["temp_c"]
        desc = data["current"]["condition"]["text"]

        print(f"{city}/{country} {time} Weather: {temp} Celsius, {desc}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
