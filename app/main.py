from dotenv import load_dotenv
import requests
import os

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if api_key:
        response_json = requests.get(f"{URL}?key={api_key}&q={CITY}").json()
        print(f"Celsius: {response_json['current']['temp_c']}")
        print(f"Fahrenheit: {response_json['current']['temp_f']}")
    else:
        print("Please, provide your API key!")


if __name__ == "__main__":
    get_weather()
