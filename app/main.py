import requests
import os


class WeatherAPIError(Exception):
    """Raised when WeatherAPI returns an error response."""
    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(f"WeatherAPI error {code}: {message}")


def get_weather(city: str = "Paris", aqi: bool = True) -> dict:

    API_KEY = os.environ.get("API_KEY")
    if not API_KEY:
        raise SystemExit("ERROR: API_KEY environment variable is not set.")

    BASE_URL = "https://api.weatherapi.com/v1"
    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "yes" if aqi else "no",
    }

    print(f"Performing request to Weather API for city {city}...")
    response = requests.get(f"{BASE_URL}/current.json",
                            params=params, timeout=10)

    if not response.ok:
        error = response.json()["error"]
        raise WeatherAPIError(error["code"], error["message"])

    return response.json()


def print_weather(data: dict) -> None:
    location = data["location"]
    current = data["current"]
    print(
        f"{location['name']}/{location['country']} "
        f"{location['localtime']} "
        f"Weather: {current['temp_c']} Celsius, {current['condition']['text']}"
    )


if __name__ == "__main__":
    weather_data = get_weather()
    print_weather(weather_data)
