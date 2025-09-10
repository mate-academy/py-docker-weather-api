import os
from requests import request

from dotenv import load_dotenv


load_dotenv()
API_KEY = os.environ["API_KEY"]
url = "https://api.weatherapi.com/v1/current.json"


def print_weather_info(data: dict) -> None:
    location = data.get("location")
    current = data.get("current")
    condition = current.get("condition")

    print(
        f"{location["name"]}/{location["country"]} "
        f"{location["localtime"]} Weather: "
        f"{current["temp_c"]} Celsius, {condition["text"]}"
    )


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")
    response = request(
        method="POST",
        url=url,
        params={
            "key": API_KEY,
            "q": "Paris",
            "lang": "en"
        }
    )
    if response.status_code != 200:
        raise ValueError("Request error")
    print_weather_info(response.json())


if __name__ == "__main__":
    get_weather()
