import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1"
DEFAULT_CITY = "Paris"

if not API_KEY:
    raise ValueError("API_KEY is missing in environment variables")


class WeatherAPIError(Exception):
    """Raised when WeatherAPI returns an error response."""
    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(f"WeatherAPI error {code}: {message}")


def get_weather(location: str = DEFAULT_CITY) -> dict:
    params = {
        "key": API_KEY,
        "q": location,
    }
    response = requests.get(
        f"{BASE_URL}/current.json",
        params=params,
        timeout=10
    )

    if not response.ok:
        error = response.json()["error"]
        raise WeatherAPIError(error["code"], error["message"])

    return response.json()


if __name__ == "__main__":
    print("Performing request to Weather API for city Paris")
    data = get_weather()
    loc = data["location"]
    cur = data["current"]

    print(
        f'{loc["name"]}/{loc["country"]} '
        f'{loc["localtime"]} '
        f'Weather: {cur["temp_c"]} Celsius, '
        f'{cur["condition"]["text"]}'
    )
