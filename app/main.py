import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
api_key = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(f"{URL}key={api_key}&q={FILTERING}")
    result = response.json()
    print(
        f'{result["location"]["name"]}/{result["location"]["country"]} '
        f'{result["location"]["localtime"]} Weather: '
        f'{result["current"]["temp_c"]} Celsius, '
        f'{result["current"]["condition"]["text"]}'
    )


if __name__ == "__main__":
    get_weather()
