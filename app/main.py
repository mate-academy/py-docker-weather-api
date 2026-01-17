import os
import requests

from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv("API_KEY")
CITY = "Paris"
BASE_URL = f"https://api.weatherapi.com/v1/current.json?q={CITY}"


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY}...")
    res = requests.get(
        BASE_URL,
        {
            "key": API_KEY,
        }
    )
    res_json = res.json()
    print(
        f"{res_json['location']['name']}/{res_json['location']['country']} "
        f"{res_json['location']['localtime']} "
        f"Weather: {res_json['current']['temp_c']} Celsius, "
        f"{res_json['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
